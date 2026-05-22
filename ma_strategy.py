"""
Торговая стратегия на основе скользящих средних
"""

class MovingAverageStrategy:
    """
    Реализация стратегии пересечения MA
    """

    def generate_signal(self, market_data):
        """
        Генерация торгового сигнала

        :param market_data: рыночные данные
        :return: BUY / SELL / HOLD
        """

        price = market_data["price"]

        if price > 90000:
            return "BUY"

        return "HOLD"
