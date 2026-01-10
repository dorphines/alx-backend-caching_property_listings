from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    data = []
    for p in properties:
        data.append({
            'title': p.title,
            'description': p.description,
            'price': p.price,
            'location': p.location,
            'created_at': p.created_at
        })
    return JsonResponse(data, safe=False)