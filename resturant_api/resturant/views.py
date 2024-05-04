from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuItemDetail(APIView):
    def get(self, request, name):
        try:
            menu_item = MenuItem.objects.get(name=name)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data)
        except MenuItem.DoesNotExist:
            return Response({"message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)
