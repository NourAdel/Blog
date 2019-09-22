from django.contrib import admin
from django.conf.urls import url, include
from posts import urls


urlpatterns = {
    url(r'admin/', admin.site.urls),
    url(r'posts/$', posts.urls),
}
