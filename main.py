# Importing the custom exception class `SensorException` from the `sensor` folder (presumably defined in `__init__.py` or another file).
# Importing `SensorException` from `sensor.Exception` means there's a module named `sensor` and inside it, there's a submodule or class named `Exception`.
from sensor.exception import SensorException

# Importing the `os` module, which provides functions for interacting with the operating system.
import os

# Importing the `sys` module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
import sys

from sensor.logger import logging

# Defining a function named `test_exception`.
def test_exception():
    # Using a try-except block to catch exceptions.
    try:
        logging.INFO("Yahan pa ek to error aie gi one devide by zero wali error")
        # Trying to execute code that may raise an exception.
        a = 1 / 0  # This line will raise a ZeroDivisionError intentionally.
    except Exception as e:
        # If an exception is caught, raise a `SensorException` with the caught exception (`e`) and `sys` (the system module) as the error details.
        raise SensorException(e, sys)

# The standard boilerplate to run the script when executed directly.
if __name__ == '__main__':
    try:
        # Call the `test_exception` function.
        test_exception()
    except Exception as e:
        # If any exception occurs during the execution of `test_exception`, print the exception.
        print(e)
