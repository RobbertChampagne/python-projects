# python logging/jsonConfigLogging.py

import logging
import logging.config
import json

def main():
    # Load logging configuration from JSON file
    with open('logging/logging_config.json', 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)

    # Log messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == '__main__':
    main()