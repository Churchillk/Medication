from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class Medicine(models.Model):
    Disease = models.CharField(max_length = 50, null = False)
    Medication = models.TextField(null = False)
    Dose = models.CharField(max_length = 50, null = False)
    start = models.DateTimeField(default = timezone.now)
    end = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    
    def __str__(self):
        return f'{self.author} profile'
    
    def get_absolute_url(self):
        return reverse('med_details', kwargs={'pk' : self.pk})