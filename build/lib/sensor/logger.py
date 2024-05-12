# A "Logger File" might contain code to configure logging handlers, formatters, and loggers to capture information about the application's behavior during runtime.
# Project tracking during runtime


# Importing the logging module, which provides a flexible framework for emitting log messages from Python programs.
import logging
# Importing the os module, which provides a way of interacting with the operating system.
import os
# Importing the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import sys
# Importing the datetime module, which provides classes for manipulating dates and times.
from datetime import datetime

# Defining a constant LOG_FILE which holds the current timestamp as part of the log file name.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Constructing the path where the log file will be stored by joining the current working directory, "logs", and the generated log file name.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Creating the directory to store logs if it doesn't already exist.
os.makedirs(logs_path, exist_ok=True)

# Constructing the full path to the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module with basic configuration.
logging.basicConfig(
    # Setting the filename to write the log messages to.
    filename=LOG_FILE_PATH,
    # Specifying the format of the log messages, including the timestamp, line number, logger name, log level, and message.
    format="[%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s",
    # Setting the logging level to INFO, which means all messages with a severity level of INFO or higher will be logged.
    level=logging.INFO,
)