from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator


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
    context = {'title': object.title, 'object': object}
    return render(request, 'post_details.html', context)


def posts_list(request):
    objlist = Post.objects.all()
    paginator = Paginator(objlist, 9) # Show 9 contacts per page
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

