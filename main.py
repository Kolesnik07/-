"""
Главный модуль запуска системы автоматизации трейдинга
"""

from core.trading_engine import TradingEngine

def main():
    """
    Точка входа в приложение
    """
    engine = TradingEngine()
    engine.start()

if __name__ == "__main__":
    main()
