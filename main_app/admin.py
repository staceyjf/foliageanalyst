from django.contrib import admin

from .models import Plants, PlantCare, Carer

# set up admin portal connection
admin.site.register(Plants)
admin.site.register(PlantCare)
admin.site.register(Carer)