import logging as log

#log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/Bar_Cafe.log'),
                    log.StreamHandler()
                ])


def debug(*message):
    log.debug(genera_mensaje(message))


def info(*message):
    log.info(message)


def warn(*message):
    log.warning(message)


def error(*message):
    log.error(message)


def critical(*message):
    log.critical(message)


def genera_mensaje(mensajes):
    reply = ""
    for mensaje in mensajes:
        reply += str(mensaje)

    return reply

info("name:",__name__)

if __name__ == '__main__':
    debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')


