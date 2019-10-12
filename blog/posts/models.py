from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# post.objects.all(), post..objects.create are PostManagers
# here we can override them or make new ones


class PostManager(models.Manager):
    def active(self):
        return super(PostManager,self).filter(draft=False).filter(publish__lte= timezone.now())


class Post (models.Model):
    # associating posts with user, admin buy default, if the user is deleted the post will be deleted too
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, default='-')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now_add=False, auto_now=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    cover = models.ImageField(null=True, blank=True, upload_to="media/")

    # connecting the manager to our model
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={'slug':self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

# a function that gets executed before the object is saved to the database


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exist = Post.objects.filter(slug=slug).exists()
    if exist:
        id = Post.objects.latest('id').id +1
        slug = "%s-%s" % (slug, str(id))
    instance.slug = slug


pre_save.connect(pre_save_post_receiver,sender=Post)
