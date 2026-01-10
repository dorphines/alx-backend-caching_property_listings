from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

def get_all_properties():
    queryset = cache.get('all_properties')
    if queryset is None:
        queryset = Property.objects.all()
        list(queryset) # Force evaluation to cache results
        cache.set('all_properties', queryset, 3600)
    return queryset

def get_redis_cache_metrics():
    con = get_redis_connection("default")
    info = con.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0

    metrics = {
        'hits': hits,
        'misses': misses,
        'hit_ratio': hit_ratio
    }
    
    # Simple print or logger? Instructions say "Log metrics".
    # I'll use a basic logger.
    logger = logging.getLogger(__name__)
    logger.info(f"Redis Metrics: {metrics}")
    
    return metrics