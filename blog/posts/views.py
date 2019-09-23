from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages


def posts_create (request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form}
    return render(request, 'post_form.html', context)


def posts_detail(request, ID):
    object = get_object_or_404(Post, id=ID)
    context = {'title': object.title, 'object': object}
    return render(request, 'post_details.html', context)


def posts_list(request):
    objlist = Post.objects.all()
    context = {'title': 'list', 'objects': objlist}
    return render(request, 'index.html', context)


def posts_update (request, ID):
    instance = get_object_or_404(Post, id=ID)
    form = PostForm(request.POST or None, instance= instance)
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

