from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

def get_all_properties():
    """
    Fetch all properties from cache or database.
    """
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        list(properties)  # Force evaluation for caching
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    """
    Connect to Redis via django_redis and retrieve keyspace hits/misses.
    Calculate hit ratio and log metrics.
    """
    logger = logging.getLogger(__name__)
    try:
        connection = get_redis_connection("default")
        info = connection.info()
        hits = int(info.get('keyspace_hits', 0))
        misses = int(info.get('keyspace_misses', 0))
        
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0
        
        metrics = {
            'hits': hits,
            'misses': misses,
            'hit_ratio': hit_ratio
        }
        logger.info(f"Redis Cache Metrics: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis metrics: {e}")
        return {'hits': 0, 'misses': 0, 'hit_ratio': 0}
