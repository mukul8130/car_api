from django.contrib import admin
from .models import category_table
# Register your models here.
@admin.register(category_table)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name')
    prepopulated_fields={'slug':('category_name',)}