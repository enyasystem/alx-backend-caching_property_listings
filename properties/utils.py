from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property
import logging

logger = logging.getLogger(__name__)


def get_all_properties():
    """Return all properties, caching the queryset in Redis for 1 hour."""
    cached = cache.get('all_properties')
    if cached is not None:
        return cached

    qs = list(Property.objects.all())
    cache.set('all_properties', qs, 3600)
    return qs


def get_redis_cache_metrics():
    """Return Redis keyspace hits/misses and hit ratio."""
    try:
        conn = get_redis_connection('default')
        info = conn.info()

        hits = int(info.get('keyspace_hits', 0))
        misses = int(info.get('keyspace_misses', 0))
        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0
        metrics = {'hits': hits, 'misses': misses, 'hit_ratio': hit_ratio}
        logger.info('Redis cache metrics: %s', metrics)
        return metrics
    except Exception as e:
        logger.error('Failed to get redis metrics: %s', e)
        logger.exception('Failed to get redis metrics: %s', e)
        return {'hits': 0, 'misses': 0, 'hit_ratio': 0}
