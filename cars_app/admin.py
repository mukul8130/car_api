from django.contrib import admin
from .models import cars_table
# Register your models here.
@admin.register(cars_table)
class CarAdmin(admin.ModelAdmin):
    list_display=('id','car_image','car_name','car_title','car_price','car_category')
    prepopulated_fields={'slug':('car_name',)}