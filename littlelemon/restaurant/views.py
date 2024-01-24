# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.decorators import api_view
# from .models import MenuItem
# from .serializers import MenuItemSerializer 

from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Menu
from .serializers import MenuItemSerializer
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

from django.contrib.auth.models import Group, User

from rest_framework import viewsets
from rest_framework import status



# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):

    # Class handles the POST and GET method calls
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # search_fields = ['category__title']
    ordering_fields = ['Price', 'Inventory']

    def get_permissions(self):
        permission_classes = []
        # if self.request.method != 'GET':
            # permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    # class is responsible for processing GET, PUT and DELETE method calls
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permission_classes = []
        # if self.request.method != 'GET':
        #     permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

