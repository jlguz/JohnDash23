from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users import urls


def home(request):
      return render(request, 'home/index.html')