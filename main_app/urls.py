# setting up the path and connecting to the views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>', views.plant_detail, name='details'),
    # CBVs
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    # related tables - PlantCare
    path('plants/<int:plant_id>/add_care/', views.add_care, name='add_care'),
    # associating carers with plants
    path('plants/<int:plant_id>/assoc_carer/<int:carer_id>/', views.assoc_carer, name='assoc_carer'),
    # removing carers with plants
    path('plants/<int:plant_id>/remove_carer/<int:carer_id>/', views.remove_carer, name='remove_carer'),
    # carers CBVs
    path('carers/', views.CarerList.as_view(), name='carers_index'),
    path('carers/<int:pk>/', views.CarerDetail.as_view(), name='carers_detail'),
    path('carers/create/', views.CarerCreate.as_view(), name='carers_create'),
    path('carers/<int:pk>/update/', views.CarerUpdate.as_view(), name='carers_update'),
    path('carers/<int:pk>/delete/', views.CarerDelete.as_view(), name='carers_delete'),
    # associating carers with photos
    path('carers/<int:carer_id>/add_photo/', views.add_photo, name='add_photo'),
]
