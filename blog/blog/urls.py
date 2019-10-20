from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django_markdown import flatpages


admin.autodiscover()

flatpages.register()

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'posts/', include('posts.urls')),
    url(r'markdown/', include('django_markdown.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
