from django.db import models
# import reserve for get_absolute_url
from django.urls import reverse
#importing a validator
from django.core.validators import MinValueValidator
# adding the date
from datetime import timedelta, datetime

FERTILIZER = (
    ('L', 'Liquid'),
    ('S', 'Slow release pellets'), 
    ('N', 'N/A'),
)


 ####### CARER  ###########
class Carer(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    #overwrite __str__
    def __str__(self):
        return self.name
    
    # define get_absolute_url with carer.id params
    def get_absolute_url(self):
        return reverse('carers_detail', kwargs={'pk': self.id})


 ####### PHOTO  ###########
class Photo(models.Model):
    url = models.CharField(max_length=200)
    carer = models.ForeignKey(Carer, on_delete=models.CASCADE) 
    #delete a carer it deletes the photos with the on_delete

    def __str__(self):
        return f"Photo for carer id: {self.carer_id} @ {self.url}"


 ####### PLANT  ###########
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
    # create the carer Model
    carers = models.ManyToManyField(Carer)

    def __str__(self):
        return f'{self.name} is a {self.plant_type} and is plant number {self.id}'
    
    # for redirecting where :id is required in URL (could use success_url - think DRY)
    def get_absolute_url(self):
        return reverse('details', kwargs={'plant_id': self.id})
    
    #logic to see if the plant has been watered in the last 7 days
    # adding on __gte for greater than or equal to 7 days ago
    def watered_this_week(self):
        seven_days_ago = datetime.now() - timedelta(weeks=1)
        return self.plantcare_set.filter(date__gte=seven_days_ago).exists()
    
class PlantCare(models.Model):
    date = models.DateField('watering date')
    water_amount = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        validators=[MinValueValidator(0)])
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
    
    class Meta:
        ordering = ['-date']
