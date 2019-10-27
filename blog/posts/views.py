from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from comments.forms import CommentForm


def posts_create (request):
    # to make sure the user is an admin or a staff member
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user     # the post user will be the request user
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, 'post_form.html', context)


def posts_detail(request, slug):
    object = get_object_or_404(Post,slug=slug)
    if object .publish > timezone.now().date() or object.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            return Http404
    initial_data = {
        'content_type': object.get_content_type,
        'obj_id': object.id,
    }

    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        c_type = comment_form.cleaned_data.get('content_type')
        content_Type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('obj_id')
        content_data = comment_form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_Type,
            object_id= obj_id,
            content = content_data
        )
    comments = Comment.objects.filter_by_instance(object)
    context = {'title': object.title, 'object': object, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'post_details.html', context)


def posts_list(request):
    objlist = Post.objects.active()
    if  request.user.is_staff or  request.user.is_superuser:
        objlist =Post.objects.all()

    # next 8 lines: filtering the posts list by the search text
    query = request.GET.get("search")
    if query:
        objlist = objlist.filter(
            Q(title__icontains= query)|
            Q(content__icontains= query)|
            Q(user__first_name__icontains= query)|
            Q(user__last_name__icontains= query)
            ).distinct()
    paginator = Paginator(objlist, 3)  # Show 9 contacts per page
    p = " POSTS"
    page = request.GET.get(p)
    objlist = paginator.get_page(page)
    context = {'objects': objlist, 'p':p}
    return render(request, 'post_list.html', context)


def posts_update (request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Edit saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form, 'title': instance.title, 'instance': instance}
    return render(request, 'post_form.html', context)


def posts_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        return Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "DELETED")
    return redirect("posts:list")

