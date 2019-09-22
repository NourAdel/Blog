from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin (admin.ModelAdmin):
    # post attributes displayed to the admin
    list_display = ["title", "updated", "timestamp"]

    # post attributes ???? to the admin
    list_display_links = ["updated", "timestamp"]
    # post attributes the admin can edit
    list_editable = ["title"]
    # post attributes the admin can search in
    list_filter = ["title", "content"]


    class Meta:
        model = Post
admin.site.register(Post)
