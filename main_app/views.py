from django.shortcuts import render

# model import - best practice is to call it singular which I will have to do next time
from .models import Plants

# Created views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  plants = Plants.objects.all() # creating the all dict from Plants model
  return render(request, 'plants/index.html', {
    'plants': plants # sharing it with the template
  })

# need additional args to accept the additional URL params
# make sure it matches in the urls.py
def plant_detail(request, plant_id):
  # define your variable, get() is like getOne in mongoose 
  # pass in the id to identify the object
  plant = Plants.objects.get(id=plant_id)
  return render(request, 'plants/details.html', {
     'plant': plant # sharing it with the template
  })