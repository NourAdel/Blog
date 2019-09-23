from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.


def posts_create (request):
    return HttpResponse("hello")


def posts_detail(request, ID):
    object = get_object_or_404(Post, id=ID)
    context = {'title': object.title, 'object': object}
    return render(request, 'post_details.html', context)


def posts_list(request):
    objlist = Post.objects.all()
    context = {'title': 'list', 'objects': objlist}
    return render(request, 'index.html', context)


def posts_update (request):
    return HttpResponse("hello")


def posts_delete(request):
    return HttpResponse("hello")
