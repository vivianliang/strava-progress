from django.shortcuts import render


def index(request):
  print '!!!!!!!!!!!!!!!!!!!'
  print request
  print request.user
  print '~~~~~~~~~~~~~~~~~~~'
  return render(request, 'index.html')
