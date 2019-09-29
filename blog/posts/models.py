from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.


class Post (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, default='-')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    cover = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'slug':self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exist = Post.objects.filter(slug=slug).exists()
    if exist:
        id = Post.objects.latest('id').id +1
        slug = "%s-%s" % (slug, str(id))
    instance.slug = slug


pre_save.connect(pre_save_post_receiver,sender=Post)
