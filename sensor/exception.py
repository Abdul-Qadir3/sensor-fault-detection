import sys # "sys" provides access to system-specific parameters and functions,
import os # "os" provides operating system-dependent functionality, allowing interaction with the operating system

# Define a function called error_message_detail which takes two arguments:
# `error` (the error message) and `error_detail` (details about the error, of type sys).
# error in the line and error in the folder
def error_message_detail(error, error_detail:sys):

    # Get the traceback object using the `exc_info()` method from the `error_detail` parameter.
    # line no of error, error in which file
    # first twi things are not impoetant so we use it in _,_
    _, _, exc_tb = error_detail.exc_info() # this function will captures error detail
    
    # Extract the filename from the traceback object.
    filename = exc_tb.tb_frame.f_code.co_filename

    # "exc_tb.tb_lineno" use to capture line number of error
    # Create an error message string containing details about the error, filename, and line number.
    error_message = "Error occurred and the file name is [{0}] and the line number is [{1}] and error is [{2}]".format(filename, exc_tb.tb_lineno, str(error))
    return error_message

# Define a custom exception class named SensorException, which inherits from the built-in Exception super-class.
class SensorException(Exception):  # Exception is a superclass

    #make a constructor inside class
    # Define the constructor using (__init__) method for the SensorException class.
    # It takes two arguments: `error_message` (the error message) and `error_detail` (details about the error, of type sys).
    def __init__(self, error_message, error_detail:sys):
        
        # Call the constructor of the superclass (Exception) and pass the `error_message` to it using super function.
        # super is used to inherit the exception class
        super().__init__(error_message)
        
        # Store the formatted error message by calling the `error_message_detail` function.
        # Pass the `error_message` and `error_detail` to it.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Define the __str__ method to provide a string representation of the exception.
    # Dendor function(to represent anything in string)
    def __str__(self):
        # Return the formatted error message.
        return self.error_message
    


    # To capture the errors we used the exception class 
    # To capture the error detailswe used "error_message_detail" function
    # to run this file we use "main.py" and import this file 
