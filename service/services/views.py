from django.db.models import Prefetch, F, Sum
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from service.settings import PRICE_CACHE_NAME
from services.models import Subscription
from services.serializers import SubscriptionSerializer
from django.core.cache import cache


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')),
    )
    serializer_class = SubscriptionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        responce = super().list(request, *args, **kwargs)

        price_cache=cache.get(PRICE_CACHE_NAME)
        if price_cache:
            total_price=price_cache
        else:
            total_price=queryset.aggregate(total=Sum('price')).get('total')
            cache.set(PRICE_CACHE_NAME,total_price,60*60)
        responce_data = {'result': responce.data}
        responce_data['total_amount']=queryset.aggregate(total=Sum('price')).get('total')
        responce.data=responce_data
        return responce

