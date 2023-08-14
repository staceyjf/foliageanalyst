from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# model import - best practice is to call it singular which I will have to do next time
from .models import Plants

# Created views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
  plants = Plants.objects.all().order_by('is_healthy','name') # creating the all dict from Plants model
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

class PlantCreate(CreateView):
   model = Plants
   fields = '__all__'
   # need all the fields to add a plant

class PlantUpdate(UpdateView):
   model = Plants
   fields = ['plant_type', 'location', 'is_healthy']
   # don't want them to edit the plant name

class PlantDelete(DeleteView):
   model = Plants
   success_url = '/plants'
   # once the details page is detailed, redirect to the all plants page