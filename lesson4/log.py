import logging

formatt = '[%(levelname)s] %(asctime).19s [%(filename)s:%(lineno)d] %(message)s'

logging.basicConfig(
    level=logging.DEBUG,
    format=formatt
)

logger = logging.getLogger()

logger.info('Информационное сообщение')
