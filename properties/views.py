from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from .utils import get_all_properties, get_redis_cache_metrics

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    return render(request, 'properties/property_list.html', {'properties': properties})

def cache_metrics_view(request):
    metrics = get_redis_cache_metrics()
    return JsonResponse({
        "hits": metrics.get('hits', 0),
        "misses": metrics.get('misses', 0),
        "hit_ratio": metrics.get('hit_ratio', 0)
    })
