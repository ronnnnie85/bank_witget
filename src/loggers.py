import logging


def create_logger(
    name_logger: str, name_log_file: str, logging_level: int
) -> logging.Logger:
    """Функция создания логера для модулей"""
    logger = logging.getLogger(name_logger)
    logger.setLevel(logging_level)

    file_handler = logging.FileHandler(
        name_log_file, mode="w", encoding="utf-8"
    )
    file_handler.setLevel(logging_level)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(file_formatter)

    logger.addHandler(file_handler)

    return logger
