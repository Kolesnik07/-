"""
Основной движок торговой системы
"""

from strategies.ma_strategy import MovingAverageStrategy
from utils.logger import setup_logger

class TradingEngine:
    """
    Класс управления торговой системой
    """

    def __init__(self):
        self.logger = setup_logger()
        self.strategy = MovingAverageStrategy()

    def start(self):
        """
        Запуск торгового цикла
        """
        self.logger.info("Система запущена")

        market_data = {
            "price": 100000
        }

        signal = self.strategy.generate_signal(market_data)

        self.logger.info(f"Получен сигнал: {signal}")
