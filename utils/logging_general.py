import logging as log

#log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('../logs/.log'),
                    log.StreamHandler()
                ])