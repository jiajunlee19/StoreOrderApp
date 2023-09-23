import logging
import os


def logger_init(filename, folder='Logs', mode='a'):
    """Init logger, with console/file writer"""

    # loglevel could be one of these: ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    # Create Logs/ folder if not exists
    if not os.path.exists(folder):
        os.makedirs(folder)

    # create logger
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - #%(lineno)d - %(filename)s -> %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # create File handler
    fh = logging.FileHandler(encoding='utf-8', filename=f"{folder}/{filename}", mode=mode)

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    # add formatter
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


if __name__ == "__main__":
    # Happy Logging!
    log = logger_init('example.log', 'Logs', 'a')
    log.debug('debug message')
    log.info('info message')
    log.warning('warn message')
    log.error('error message')
    log.critical('critical message')
