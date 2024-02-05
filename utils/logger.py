import logging

# Configuring basic logging settings like filename, log format, etc.
logging.basicConfig(filename='newsextractor.log',format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO)


def log_message(message: str, level: int):
    """
    logging function

    Args:
        message (str): message
        level (int): level (error=1, info=0)

    Returns:
        log file
    """

    # decides the type of message to be printed
    if level == 1:
        logging.error(message)
    elif level == 0:
        logging.info(message)