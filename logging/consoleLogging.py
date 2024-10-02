# python logging/consoleLogging.py

import logging

def main():
    # Configure the logging
    logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')

    # Log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()