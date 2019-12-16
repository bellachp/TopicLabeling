## TopicLabeling

Project info

The script makes use of various classes and files in the model folder.


#### Dependencies
Dependencies are managed via virtual environment requirements file. The project makes extensive use of the following open-source libraries:

* https://numpy.org/
* https://pandas.pydata.org/
* https://scikit-learn.org/stable/
* https://xgboost.readthedocs.io/en/latest/

Specific versions can be found in the requirements.txt file.


#### virtual environment and setup
install a virtual environment in your preferred way and use pip to install from the requirements file.

example. from command line:
```
pip install virtualenv
```

navigate to directory desired

```
virtualenv -p python3 [pathToDir, or . if already there]
```

activate it
```
source [pathToDir]/Scripts/activate ## windows
source [pathToDir]/bin/activate ## *nix
```

install from requirements
```
pip install -r requirements.txt
```


#### style
Flake8 and PEP8 are used to check and enforce most python code best practices. Documentation and style guide can be found at the following pages:

http://flake8.pycqa.org/en/latest/

https://www.python.org/dev/peps/pep-0008/


###### contact
```
url='https://github.com/bellachp/TopicLabeling'
author='chris bellavia'
author_email=''
```
