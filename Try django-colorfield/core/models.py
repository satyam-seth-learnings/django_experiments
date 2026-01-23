from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class ExampleModel(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    image = models.ImageField(upload_to="images")
    color = ColorField(image_field="image")
    hex_color = ColorField(default='#FF0000')
    hexa_color = ColorField(format="hexa")
    rgb_color = ColorField(format="rgb")
    rgba_color = ColorField(format="rgba")
    restrictive_color = ColorField(choices=COLOR_PALETTE)
    non_restrictive_color = ColorField(samples=COLOR_PALETTE)