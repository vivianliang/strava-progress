from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from .api import get_starred_segments
from .models import Segment, StarredSegment


def index(request):
  return render(request, 'index.html')


def logout(request):
  auth_logout(request)
  return redirect('/')


def refresh_starred_segments(request):
  segment_data = get_starred_segments(request.user)
  starred_segment_ids = []
  for segment in segment_data:
    starred_segment_ids.append(segment['id'])
    segment_object = Segment.objects.get_or_create(id=segment['id'], name=segment['name'])
    StarredSegment.objects.get_or_create(user=request.user, segment=segment_object[0])

  # remove no longer starred segments
  (StarredSegment.objects
    .filter(user=request.user)
    .exclude(segment_id__in=starred_segment_ids)
    .delete())
  return redirect('/')
