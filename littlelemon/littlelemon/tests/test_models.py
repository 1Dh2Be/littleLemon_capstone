from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenu(TestCase):
    def test_create_item(self):
        item = Menu.objects.create(title='iceCream', price='80', inventory=100)
        self.assertEqual(str(item), 'iceCream : 80$')

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu items
        Menu.objects.create(title='Ice Cream', price=80.00, inventory=100)
        Menu.objects.create(title='Pizza', price=120.00, inventory=50)
        Menu.objects.create(title='Burger', price=90.00, inventory=75)

    def test_getall(self):
        # Get all Menu objects
        menus = Menu.objects.all()

        # Serialize the Menu objects
        serializer = MenuSerializer(menus, many=True)

        # Make a GET request to the endpoint
        response = self.client.get('/restaurant/menu-items/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
