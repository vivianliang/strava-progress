from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from .api import get_starred_segments, get_segment_efforts
from .models import Effort, Segment, StarredSegment


def index(request):
  return render(request, 'index.html')


def logout(request):
  auth_logout(request)
  return redirect('/')


def segment(request, segment_id):
  segment = Segment.objects.get(id=segment_id)
  return render(request, 'segment.html', {'segment': segment})


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


def refresh_segment_efforts(request, segment_id):
  effort_data = get_segment_efforts(request.user, segment_id)

  for effort in effort_data:
    if not Effort.objects.filter(id=effort['id']).exists():
      Effort.objects.create(
      id=effort['id'],
      name=effort['name'],
      user=request.user,
      segment_id=effort['segment']['id'],
      elapsed_time=effort['elapsed_time'],
      moving_time=effort['moving_time'],
      start_date=effort['start_date'])
  return redirect('/segment/%s' % segment_id)
