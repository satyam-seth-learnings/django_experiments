from django.shortcuts import render
from .models import Product
from django.utils.translation import get_language

def product_detail(request, product_id): 
    language_code = request.GET.get("lang", "en")
    product = Product.objects.get(id=product_id)

    # Fetch the translated fields based on the current language
    translated_name = product.safe_translation_getter("name", language_code=language_code)
    translated_description = product.safe_translation_getter("description", language_code=language_code)

    return render(request, "products/product_detail.html", {
        "product": product,
        "name": translated_name,
        "description": translated_description,
        "lang": language_code,
    })
