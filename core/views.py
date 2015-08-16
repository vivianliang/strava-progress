from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render


def index(request):
  return render(request, 'index.html')

def logout(request):
  auth_logout(request)
  return redirect('/')
