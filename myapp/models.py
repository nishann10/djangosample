from django.db import models

# Create your models here.

class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=10)
    user_place=models.CharField(max_length=20)    



    