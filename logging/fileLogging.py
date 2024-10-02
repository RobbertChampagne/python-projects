# python logging/fileLogging.py

import logging

def main():
    # Configure the logging
    logging.basicConfig(
        level=logging.WARNING, 
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logging/output.log'
    )

    # Log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()