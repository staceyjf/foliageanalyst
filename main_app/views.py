import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from bootstrap_datepicker_plus.widgets import DateTimePickerInput

# model import - best practice is to call it singular which I will have to do next time
from .models import Plants, Carer, Photo
from .forms import CareForm

# Created views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

 ####### PLANT ###########
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
  # define the carer's assoc with a plant
  id_list = plant.carers.all().values_list('id')
  carers_assoc_with_plant = Carer.objects.exclude(id__in=id_list)

  care_form = CareForm()
  return render(request, 'plants/details.html', {
     'plant': plant, # sharing it with the template
     'care_form' : care_form,
     'carers': carers_assoc_with_plant,
  })

class PlantCreate(CreateView):
   model = Plants
   fields = ['name', 'plant_type', 'location', 'is_healthy']
   # need all the fields to add a plant

class PlantUpdate(UpdateView):
   model = Plants
   fields = ['plant_type', 'location', 'is_healthy']
   # don't want them to edit the plant name

class PlantDelete(DeleteView):
   model = Plants
   success_url = '/plants'
   # once the details page is deleted, redirect to the all plants page

# related models
# writing the code for processing the FeedingForm
def add_care(request, plant_id):
  form = CareForm(request.POST) 
  # like req.body
  if form.is_valid():
    # wait to associate before saving
    new_care = form.save(commit=False)
    new_care.plant_id = plant_id
    new_care.save()
    #need the cat id as its passed into the URL
  return redirect('details', plant_id=plant_id)

 ####### CARER ###########
class CarerList(ListView):
  model = Carer

class CarerDetail(DetailView):
  model = Carer

class CarerCreate(CreateView):
  model = Carer
  fields = '__all__'

class CarerUpdate(UpdateView):
  model = Carer
  fields = ['nickname']

class CarerDelete(DeleteView):
  model = Carer
  success_url = '/carers'

# check inspector to see the association is made from 
# the template before you write this
def assoc_carer(request, plant_id, carer_id):
  #add and remove() will also take ids 
  Plants.objects.get(id=plant_id).carers.add(carer_id)
  return redirect('details', plant_id=plant_id)

def remove_carer(request, plant_id, carer_id):
  #add and remove() will also take ids 
  Plants.objects.get(id=plant_id).carers.remove(carer_id)
  return redirect('details', plant_id=plant_id)

####### PHOTO ###########
@require_http_methods(["GET", "POST"])
def add_photo(request, pk):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # creating a unique key for each image while keeping file extension
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # store this URL in our photo object in the database
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # assign to a carer
            Photo.objects.create(url=url, carer_id=pk)
        except Exception as e:
            print('An error occurred while uploading the file to S3')
            print(e)
    return redirect('carers_detail', pk=pk)
