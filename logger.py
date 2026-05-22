"""
Модуль логирования
"""

import logging

def setup_logger():
    """
    Настройка логирования
    """

    logger = logging.getLogger("autotrader")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler("logs/system.log", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
