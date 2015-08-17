from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
  user = models.OneToOneField(User, related_name='profile', primary_key=True)
  pic = models.URLField()


def post_user_save(sender, instance, created, **kwargs):
  if not created:
    return

  Profile.objects.create(user=instance)

post_save.connect(post_user_save, sender=User, weak=False)
