from django.forms import ModelForm
from .models import PlantCare

class CareForm(ModelForm):
    class Meta:
        model = PlantCare
        fields = ['date', 'water_amount', 'give_fertilizer', 'fertilizer']