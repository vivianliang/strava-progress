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


class Segment(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.TextField()


class StarredSegment(models.Model):
  user = models.ForeignKey(User, related_name='starred_segments')
  segment = models.ForeignKey(Segment, related_name='+')
