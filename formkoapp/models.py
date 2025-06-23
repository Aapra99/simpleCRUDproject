
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db import models

class options(models.TextChoices):
    Male='M'
    Female='F'

class FormData(models.Model):
    name=models.CharField(max_length=30,validators=[MaxLengthValidator(30),MinLengthValidator(5)])
    age=models.IntegerField(validators=[MaxValueValidator(35),MinValueValidator(18)])
    sex=models.CharField(max_length=1,choices=options.choices)
