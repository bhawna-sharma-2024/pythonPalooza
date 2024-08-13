import logging

def setup_logging():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,  # Adjust the logging level as needed
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        filename='test_log.log',
        handlers=[
            logging.FileHandler('test_log.log',mode="a", encoding="utf-8"),
            logging.StreamHandler()  # Also log to the console
        ]

    )
    return logger