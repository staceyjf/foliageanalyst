from django.contrib import admin

from .models import Plants, PlantCare, Carer, Photo

# set up admin portal connection
admin.site.register(Plants)
admin.site.register(PlantCare)
admin.site.register(Carer)
admin.site.register(Photo)