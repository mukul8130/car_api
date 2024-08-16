from django.db import models
from cars_category.models import category_table
# Create your models here.

class cars_table(models.Model):
    car_image=models.ImageField()
    car_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    car_title=models.CharField(max_length=100)
    car_price=models.IntegerField()
    car_category=models.ForeignKey(category_table,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name



