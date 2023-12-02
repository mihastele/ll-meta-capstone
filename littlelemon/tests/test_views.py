from django.test import TestCase
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item2 = Menu.objects.create(title="Burek", price=6.77, inventory=20)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/items/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
