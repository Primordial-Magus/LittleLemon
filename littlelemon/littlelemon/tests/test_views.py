from django.test import TestCase
from restaurant.views import MenuItemsView, BookingViewSet
from restaurant.models import Menu, Booking


class MenuViewTest(TestCase):

    def setUp(self):
        self.menu_items = []

        item_1 = str(Menu.objects.create(ID = 1, Title="IceCream", Price=80, Inventory=100))
        self.menu_items.append(item_1)
        item_2 = str(Menu.objects.create(ID = 2, Title="Toast", Price=90, Inventory=10))
        self.menu_items.append(item_2)
        item_3 = str(Menu.objects.create(ID = 3, Title="Milk", Price=100, Inventory=1))
        self.menu_items.append(item_3)
        
        
    def test_get_all(self):

        concat_items = ', '.join(self.menu_items)

        self.assertEqual(concat_items, "IceCream : 80, Toast : 90, Milk : 100")
