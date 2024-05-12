# A "Logger File" might contain code to configure logging handlers, formatters, and loggers to capture information about the application's behavior during runtime.
# Project tracking during runtime after deployment
# show error without opening in an ide

# Importing the logging module, which provides a flexible framework for emitting log messages from Python programs.
import logging

# Importing the os module, which provides a way of interacting with the operating system.
import os

# Importing the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import sys

# Importing the datetime module, which provides classes for manipulating dates and times.
# tells time of error(captures time)
from datetime import datetime

# Defining a constant LOG_FILE which holds the current timestamp as part of the log file name.
# make a file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"#strftime the format converts to string

# Constructing the path where the log file will be stored by joining the current working directory, "logs", and the generated log file name.
# will make path for file 
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # logs = filname , catures current working directory

# Creating the directory to store logs if it doesn't already exist.
# makes folder/directory and handle folder if exist no creation
os.makedirs(logs_path, exist_ok=True)   #If the directory already exists, it doesn't raise an error due to the exist_ok=True parameter. 

# Constructing the full path to the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module with basic configuration.
# this function used to capture the information required
logging.basicConfig(
    
    # Setting the filename to write the log messages to.
    filename=LOG_FILE_PATH,
    
    # Specifying the format of the log messages, including the timestamp, line number, logger name, log level, and message.
    # [%(asctime)s] capture time 
    #%(lineno)s capture line number
    #%(name)s name of logger
    # - %(levelname)s level name
    # - %(message)s messages the error
    format="[%(asctime)s] %(lineno)s %(name)s - %(levelname)s - %(message)s", # s for sring and d for digit
    
    # Setting the logging level to INFO, which means all messages with a severity level of INFO or higher(6 levelsof info are NOTSET=0.DEBUG=10.INFO=20.WARN=30.ERROR=40.CRITICAL=50.) will be logged.
    level=logging.INFO,
)



# call this file in main with in small letters the "info" word
# run using "python main.py"