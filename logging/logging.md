# Logging

In Python's logging module, log messages are categorized by severity levels.

`level=logging.WARNING`: This sets the logging threshold to **WARNING**.<br> 
Only messages with a severity level of **WARNING** or higher will be logged.<br>

Only the messages with severity levels **WARNING**, **ERROR**, and **CRITICAL** are logged and displayed because the logging level is set to **WARNING**.

`consoleLogging.py`
```Python
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
```

OUTPUT:
```Bash
WARNING - This is a warning message
ERROR - This is an error message
CRITICAL - This is a critical message
```

---

### Logging to a File

Add `filename='logging/output.log'` to the `basicConfig()` this will append the logging to the file.

`fileLogging.py`
```Python
logging.basicConfig(
        level=logging.WARNING, 
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logging/output.log'
    )
```

---

### Logging using a JSON file

To configure logging using a JSON file, you can use the logging.config module, <br>
which provides a way to configure logging via a configuration file.<br> 
Below is an example of how to set up logging configuration using a JSON file to log messages to both the console and a file.

- **version**: Specifies the version of the logging configuration schema.
- **disable_existing_loggers**: If false, existing loggers are not disabled.
- **formatters**: Defines the format of the log messages.
- **handlers**: Defines where the log messages will be output (console and file in this case).
- **loggers**: Configures the root logger to use the defined handlers and sets the logging level.

```Json
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "WARNING",
            "formatter": "standard",
            "filename": "logging/output.log",
            "mode": "a",
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["console", "file"]
        }
    }
}
```

