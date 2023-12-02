from django.test import TestCase
from .models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Burek", price=6.77, inventory=20)
        self.assertEqual(str(item), "IceCream : 80")
