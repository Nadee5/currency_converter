from rest_framework import serializers


class CurrencyConverterSerializer(serializers.Serializer):
    """
    Сериализотор для конвертации валют.
    :from_currency: Код валюты, из которой производится конвертация. Максимальная длина - 3 символа.
    :to_currency: Код валюты, в которую производится конвертация. Максимальная длина - 3 символа.
    :value: Значение суммы, для конвертации. Max количество цифр - 10, количество десятичных знаков - 2.
    """
    from_currency = serializers.CharField(max_length=3)
    to_currency = serializers.CharField(max_length=3)
    value = serializers.DecimalField(max_digits=10, decimal_places=2)


class CurrencyListAPISerializer(serializers.Serializer):
    """
    Сериализотор для списка поддерживаемых валют.
    :code: Код валюты. Максимальная длина - 10 символов.
    :name: Название валюты. Максимальная длина - 100 символов.
    """
    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
