from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='posts'

urlpatterns = [

    url(r'^create/$', views.posts_create),
    url(r'^(?P<ID>\d+)/$', views.posts_detail, name="detail"),
    url(r'^$', views.posts_list, name="list"),
    url(r'^(?P<ID>\d+)/edit/$', views.posts_update, name="update"),
    url(r'^(?P<ID>\d+)/delete/$', views.posts_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
