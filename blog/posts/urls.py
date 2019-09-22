from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^create/$', views.posts_create),
    url(r'^detail/$', views.posts_detail),
    url(r'^$', views.posts_list),
    url(r'^update/$', views.posts_update),
    url(r'^delete/$', views.posts_delete),
]
