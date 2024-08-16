from cars_app.models import cars_table
from rest_framework import serializers

class car_serializer(serializers.ModelSerializer):
    class Meta:
        model=cars_table
        fields='__all__'