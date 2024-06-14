from django.urls import path

from currency_converter.apps import CurrencyConverterConfig
from currency_converter.views import CurrencyConversionAPIView, CurrencyListAPIView

app_name = CurrencyConverterConfig.name

urlpatterns = [
    path('', CurrencyListAPIView.as_view(), name='currency_list'),
    path('api/rates/', CurrencyConversionAPIView.as_view(), name='currency_converter'),
]
