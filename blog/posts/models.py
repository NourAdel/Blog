from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from markdown_deux import markdown
from django.utils.safestring import mark_safe
# from comments.models import Comment
from django.contrib.contenttypes.models import ContentType


# post.objects.all(), post..objects.create are PostManagers
# here we can override them or make new ones


class PostManager(models.Manager):
    def active(self):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


class Post(models.Model):
    # associating posts with user, admin by default, if the user is deleted the post will be deleted too
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
        return reverse("posts:detail", kwargs={'slug': self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def get_markdown(self):
        content = self.content
        return mark_safe(markdown(content))

    # one other way to show comments, as property/method of Post
    '''
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs
'''

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

# a function that gets executed before the object is saved to the database


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exist = Post.objects.filter(slug=slug).exists()
    if exist:
        id = Post.objects.latest('id').id + 1
        slug = "%s-%s" % (slug, str(id))
    instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Post)
