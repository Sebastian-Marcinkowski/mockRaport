from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Raport(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    formatR = models.CharField(max_length=8, null=False, blank=False)
    email= models.EmailField(max_length=128, null=False, blank=True)
    scheduleType = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                                MaxValueValidator(4)], null=False)
    scheduleTime = models.CharField(max_length=5, null=True, blank=False)
    scheduleDay = models.CharField(max_length=3, null=True, blank=False)
    scheduleDate = models.CharField(max_length=10, null=True, blank=False)