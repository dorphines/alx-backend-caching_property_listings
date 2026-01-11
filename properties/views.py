from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties, get_redis_cache_metrics

@cache_page(60 * 15)
def property_list(request):
    data = get_all_properties()
    return render(request, 'properties/property_list.html', {'properties': data})

def cache_metrics_view(request):
    data = get_redis_cache_metrics()
    return JsonResponse({
        "hits": data.get('hits', 0),
        "misses": data.get('misses', 0),
        "hit_ratio": data.get('hit_ratio', 0)
    })
