from cgi import test
from django.test import TestCase
from .models import My

# Create your tests here.


class MyTestCase(TestCase):
    def setUp(self):
        My(test='hello').save()

    def test_choices(self):
        self.assertEqual(My.objects.all().count(), 1)
