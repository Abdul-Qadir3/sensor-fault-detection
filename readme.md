## To create conda environment<br>
```conda create -n myenv python=3.12.2```<br>
```conda create -p myenv python=3.12.2```<br>
* Specifies the path `(-p)` where the environment will be created. In this case, the environment named `"myenv"` will be created directly in the current directory, rather than within the Conda environment directory. This allows for more flexibility in specifying the location of the environment.
## To run setup file<br>
```pip setup.py install```<br>
## To run requirements file<br>
```pip install -r requirements.txt```

# Problem Statement of the project
![alt text](image.png)
# Solution of the problem
System/project will predict if their is an issue in `APS` system `yes or no`<br>
Two classes of binary classification positive and negative. Positive for component failer and negative for other reasons.
## `Creating folder into Pakage` to use iin the project
We use `__init__.py` pakage file can be used accessed everywhere and can be used by other modules and all the pakages are avalable in `pypi.org`


## Exception File
- An "Exception File" is not a standard term in Python. However, it could refer to a file where you handle exceptions in your Python code.
- In Python, exceptions are raised when `errors occur` during program execution. You can `catch and handle` these exceptions using `try and except` blocks.
- An "Exception File" could be where you write code to `catch and manage these exceptions`, such as logging them or displaying error messages to users.
## Logger File
- A "Logger File" typically refers to a Python `script or module` where you set up `logging` functionality.
- In Python, the logging module provides a `flexible framework` for `emitting log messages` from your application.
- A "Logger File" might contain code to configure logging handlers, formatters, and loggers to capture information about the application's behavior during runtime.
## Setup File:
All the libraries are installed through thi file.
- A "Setup File" usually refers to `setup.py`, which is a Python script used for `package distribution and installation`.
- When you develop a Python package, you create a `setup.py` file to `define metadata` about your package, such as its `name, version, author, dependencies, etc`.
- The setup.py file is `crucial` for building, distributing, and installing your Python package using tools like `pip`.
- `python setup.py install` to run one time installation in the project
## .egg-info Folder:
- The `.egg-info` folder is a `directory` created when you `install a Python package using setuptools` or distribute.
- It contains `metadata` about the `installed package`, such as its `name, version, dependencies, and other` information specified in the `setup.py` file.
- This metadata is used by `package management` tools like `pip` to manage installed packages and their dependencies.