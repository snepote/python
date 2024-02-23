# python
Python scripts playground

## Virtual Environment
Python has a feature called "virtual environments," which is a crucial tool for managing project dependencies and avoiding conflicts between different projects. A virtual environment is an isolated environment that allows Python users to maintain separate directories for different projects, ensuring that each project has its own dependencies, regardless of what dependencies every other project has.

The standard tool used for creating virtual environments in Python is venv (introduced in Python 3.3). Prior to Python 3.3, a similar tool called virtualenv was widely used, and it remains popular due to its additional features and compatibility with older versions of Python.

### Create a virtual environment
```shell
python3 -m venv env
```
This command creates a directory named env in your project directory, where env is the common naming convention for a virtual environment (but you can name it anything). This directory contains a copy of the Python interpreter, the Pip package manager, and other supporting files.

### Activate the virtual environment
```shell
source env/bin/activate
```

### Deactivate the virtual environment
```shell
deactivate
```

### Install project-specific packages
```shell
pip install package_name
```

## Run test
```shell
pytest
```