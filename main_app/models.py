from django.db import models

# import reserve for get_absolute_url
from django.urls import reverse

FERTILIZER = (
    ('L', 'Liquid'),
    ('S', 'Slow release pellets'), 
    ('N', 'N/A'),
)

# Create your models here.
class Plants(models.Model):
    name = models.CharField(max_length=100)
    plant_type = models.CharField(max_length=100)
    location = models.CharField(max_length=250, choices=[
        ('lounge', 'Lounge'),
        ('kitchen', 'Kitchen'),
        ('bedroom', 'Bedroom'),
        ('bathroom', 'Bathroom'),
        ('other', 'Other')
    ])
    is_healthy = models.BooleanField()

    def __str__(self):
        return f'{self.name} is a {self.plant_type} and is plant number {self.id}'
    
    # for redirecting where :id is required in URL (could use success_url - think DRY)
    def get_absolute_url(self):
        return reverse('details', kwargs={'plant_id': self.id})
    
class PlantCare(models.Model):
    date = models.DateField('watering date')
    water_amount = models.DecimalField(max_digits=5, decimal_places=2)
    give_fertilizer = models.BooleanField()
    fertilizer = models.CharField(
        max_length=1,
        choices=FERTILIZER,
        default=FERTILIZER[2][0],
    )
    # add the plants ForeignKey 
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_fertilizer_display()} on {self.date}"