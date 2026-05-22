"""
Модуль работы с API биржи
"""

import requests

class ExchangeAPI:

    def get_balance(self):
        """
        Получение баланса
        """
        return {
            "USDT": 1000
        }

    def place_order(self, symbol, side, quantity):
        """
        Отправка ордера
        """

        print(f"Ордер отправлен: {side} {symbol} {quantity}")
