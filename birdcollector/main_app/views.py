from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Bird

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/detail.html', { 'bird': bird })