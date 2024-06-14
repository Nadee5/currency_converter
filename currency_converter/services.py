import os

import currencyapicom
from decimal import Decimal, ROUND_HALF_UP

CLIENT = currencyapicom.Client(os.getenv('SECRET_KEY_CONVERTER'))


def get_exchange_rate(from_currency, to_currency):
    """
    Получить обменный курс между двумя валютами.

    Принимает коды двух валют, преобразует их в верхний регистр,
    и возвращает текущий обменный курс из первой валюты во вторую.

    :from_currency: Код исходной валюты в формате ISO 4217 (например, 'USD', 'EUR').
    :to_currency: Код целевой валюты в формате ISO 4217 (например, 'JPY', 'GBP').
    :return: Текущий обменный курс между указанными валютами.
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    rate_dict = CLIENT.latest(from_currency, currencies=[to_currency])
    unpacked_rate = rate_dict['data'][to_currency]['value']
    return unpacked_rate


def convert_currency(from_currency, to_currency, value):
    """
    Конвертировать сумму из одной валюты в другую на основе текущего обменного курса.

    Эта функция принимает коды двух валют и значение суммы, преобразует значение из исходной валюты в целевую
    на основе текущего обменного курса и возвращает результат, округленный до двух десятичных знаков.

    :from_currency: Код исходной валюты в формате ISO 4217 (например, 'USD', 'EUR').
    :to_currency: Код целевой валюты в формате ISO 4217 (например, 'JPY', 'GBP').
    :value: Сумма денег для конвертации.
    :return: Сконвертированная сумма, округленная до двух десятичных знаков.
    """
    rate = get_exchange_rate(from_currency, to_currency)
    rate_decimal = Decimal(str(rate))
    value_decimal = Decimal(str(value))

    result = rate_decimal * value_decimal
    rounded_result = result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return rounded_result


def get_currency_list():
    """
    Получить список доступных валют.

    Вызывает метод `client.currencies()` для получения списка всех доступных валют.

    :return: Словарь с данными о валютах.
    """
    result = CLIENT.currencies()
    return result
