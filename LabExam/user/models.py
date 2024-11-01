from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here

#creating user profile model
class UserProfileModel(models.Model):
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def clean(self):
        today = date.today()
        age = self.date_of_birth-today
        #checking if the date is in future
        if self.date_of_birth > today:
            raise ValidationError({'Date of Birth': 'Date of Birth should not be in future'})
        
        #checking if user is 18 or not
        if age <= 17:
            raise ValidationError({'Date of Birth': 'Sorry! at least 18 years required!'})