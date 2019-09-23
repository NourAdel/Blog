from django.conf.urls import url
from . import views

app_name='posts'

urlpatterns = [

    url(r'^create/$', views.posts_create),
    url(r'^(?P<ID>\d+)/$', views.posts_detail, name="detail"),
    url(r'^$', views.posts_list),
    url(r'^update/$', views.posts_update),
    url(r'^delete/$', views.posts_delete),
]
