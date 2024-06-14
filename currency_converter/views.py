from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from currency_converter.serializers import CurrencyConverterSerializer, CurrencyListAPISerializer
from currency_converter.services import convert_currency, get_currency_list


class CurrencyConversionAPIView(APIView):
    """
    Класс для конвертации валют.

    Позволяет конвертировать сумму из одной валюты в другую на основе данных,
    полученных из параметров запроса.

    Методы:
    - get: Обрабатывает GET-запросы для конвертации валюты.

    Пример использования:
    Для конвертации суммы из 'USD' в 'EUR' на сумму 100, сделайте GET-запрос:
    '/api/rates/?from_currency=USD&to_currency=EUR&value=100'

    Возвращает ответ в формате JSON с результатом конвертации или ошибкой, если
    введены неподдерживаемые валюты.
    """

    def get(self, request, *args, **kwargs):
        """
        Обработка GET-запроса для конвертации валюты.
        :request: Объект запроса.
        :return: Ответ в формате JSON с результатом конвертации или ошибкой.
        """
        serializer = CurrencyConverterSerializer(data=request.query_params)
        if serializer.is_valid():
            from_currency = serializer.validated_data['from_currency']
            to_currency = serializer.validated_data['to_currency']
            value = serializer.validated_data['value']

            converted_amount = convert_currency(from_currency, to_currency, value)
            if converted_amount is not None:
                return Response({'result': converted_amount}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Unsupported currency pair'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrencyListAPIView(generics.ListAPIView):
    """
    API endpoint для получения списка валют.

    Предоставляет список доступных валют в формате JSON.

    Сериализация: Используется сериализатор CurrencyListAPISerializer для преобразования данных о валютах.
    Пагинация: Используется пагинация PageNumberPagination с размером страницы, заданным в настройках.

    Пример использования:
        Для получения списка всех валют, сделайте GET-запрос: ''

        Возвращает список валют в формате JSON.
    """
    serializer_class = CurrencyListAPISerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        """
        Получить список всех валют.
        :return: Список словарей, каждый словарь представляет валюту с полями 'code' и 'name'.
        """
        currency_data = get_currency_list()
        currency_data = currency_data.get('data', {})
        currencies = [{'code': key, 'name': value['name']} for key, value in currency_data.items()]
        return currencies
