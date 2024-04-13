## To create conda environment<br>
```conda create -n myenv python=3.12.2```<br>
```conda create -p myenv python=3.12.2```<br>
## To run setup file<br>
```pip setup.py install```<br>
## To run requirements file<br>
```pip install -r requirements.txt```

## Exception File
- An "Exception File" is not a standard term in Python. However, it could refer to a file where you handle exceptions in your Python code.
- In Python, exceptions are raised when `errors occur` during program execution. You can `catch and handle` these exceptions using `try and except` blocks.
- An "Exception File" could be where you write code to `catch and manage these exceptions`, such as logging them or displaying error messages to users.
## Logger File
- A "Logger File" typically refers to a Python `script or module` where you set up `logging` functionality.
- In Python, the logging module provides a `flexible framework` for `emitting log messages` from your application.
- A "Logger File" might contain code to configure logging handlers, formatters, and loggers to capture information about the application's behavior during runtime.
## Setup File:
- A "Setup File" usually refers to `setup.py`, which is a Python script used for `package distribution and installation`.
- When you develop a Python package, you create a `setup.py` file to `define metadata` about your package, such as its `name, version, author, dependencies, etc`.
- The setup.py file is `crucial` for building, distributing, and installing your Python package using tools like `pip`.
## .egg-info Folder:
- The `.egg-info` folder is a `directory` created when you `install a Python package using setuptools` or distribute.
- It contains `metadata` about the `installed package`, such as its `name, version, dependencies, and other` information specified in the `setup.py` file.
- This metadata is used by `package management` tools like `pip` to manage installed packages and their dependencies.