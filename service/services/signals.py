from django.core.cache import cache
from django.db.models.signals import post_delete
from django.dispatch import receiver

from service.settings import PRICE_CACHE_NAME


@receiver(post_delete, sender=None)
def delete_cache_total_sum(*args, **kwargs):
    cache.delete(PRICE_CACHE_NAME)