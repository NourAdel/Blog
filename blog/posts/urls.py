from django.conf.urls import url
from . import views



app_name='posts'

urlpatterns = [

    url(r'^create/$', views.posts_create),
    url(r'^$', views.posts_list, name="list"),
    url(r'^(?P<slug>[-\w]+)/$', views.posts_detail, name="detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.posts_update, name="update"),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.posts_delete),
]

