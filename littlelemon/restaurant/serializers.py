from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, Menu


class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['ID', 'Name', 'No_of_guests', 'BookingDate']

class MenuItemSerializer(serializers.ModelSerializer):
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset=Category.objects.all()
    # )

    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ['ID', 'Title', 'Price', 'Inventory']
        
