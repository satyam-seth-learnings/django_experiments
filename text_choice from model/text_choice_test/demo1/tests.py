from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Demo, TEST_CHOICES

# Create your tests here.


class DemoTestCase(TestCase):
    def test_choices(self):
        rec=Demo.objects.create(my_field='dummy')
        with self.assertRaises(ValidationError):
            rec.full_clean()