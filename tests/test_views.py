from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=25, inventory=10)
        Menu.objects.create(title="Burger", price=15, inventory=20)
        Menu.objects.create(title="Salad", price=10, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)