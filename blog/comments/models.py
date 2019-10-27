from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager (models.Manager):
    def all(self):
        qs =  super(CommentManager,self).filter(parent=None)

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)  # getting the python class of the instance
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type= content_type, object_id=obj_id).filter(parent= None)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    # connecting the manager to our model
    objects = CommentManager()

    class Meta:
        ordering = ['time_stamp']

    def __str__(self):
        return str(self.user.username)

    # getting the replies to a certain comment
    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        else:
            return True
