from django.contrib import admin

from .models import Plants

# set up admin portal connection
admin.site.register(Plants)
