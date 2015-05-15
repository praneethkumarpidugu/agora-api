import uuid
from django.contrib.auth.models import User as AuthUser
from django.db import models


class User(AuthUser):
    class Meta:
        proxy = True


class Common(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Page(Common):
    name = models.TextField()

    user = models.ForeignKey(User, related_name='pages')

    def __str__(self):
        return self.name


class Comment(Common):
    text = models.TextField()

    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    user = models.ForeignKey(User, related_name='comments')
    page = models.ForeignKey(Page, related_name='comments')

    def __str__(self):
        return self.text

    def to_JSON(self):
        return {
            'id': self.id,
            'parent': self.parent.id if self.parent else None,
            'user': self.user.id,
            'page': self.page.id,
            'children': [child.to_JSON() for child in self.children.all()]
        }


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
