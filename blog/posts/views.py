from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import quote
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator


def posts_create (request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, 'post_form.html', context)


def posts_detail(request, slug):
    object = get_object_or_404(Post,slug=slug)
    # url encoded text
    sharable = quote(object.content)
    context = {'title': object.title, 'object': object, 'sharable': sharable}
    return render(request, 'post_details.html', context)


def posts_list(request):
    objlist = Post.objects.all()
    paginator = Paginator(objlist, 9) # Show 25 contacts per page
    p = " POSTS"
    page = request.GET.get(p)
    objlist = paginator.get_page(page)
    context = {'objects': objlist, 'p':p}
    return render(request, 'post_list.html', context)


def posts_update (request, slug):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Edit saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form, 'title': instance.title, 'instance': instance}
    return render(request, 'post_form.html', context)


def posts_delete(request, ID):
    instance = get_object_or_404(Post, id=ID)
    instance.delete()
    messages.success(request, "DELETED")
    return redirect("posts:list")

