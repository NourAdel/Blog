from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def posts_create (request):
    return HttpResponse("hello")


def posts_detail(request):
    return HttpResponse("hello")


def posts_list(request):
    cotext= {'title': 'list'}
    return render(request, 'index.html', cotext)


def posts_update (request):
    return HttpResponse("hello")


def posts_delete(request):
    return HttpResponse("hello")
