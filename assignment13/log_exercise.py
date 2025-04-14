import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='app.log',
                    filemode='w',
                    format='%(name)s - '
                           '%(levelname)s - '
                           '%(message)s - ')

logging.debug('This is a debug statement')
logging.debug('This will get logged to a file')
logging.debug('This is a warning')
logging.debug('This is an ERROR!')
