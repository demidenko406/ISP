from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='Lab',
    version='1.0',
    packages=['Lab', 'Lab/Factory', 'Lab/Json','Lab/Toml','Lab/Yaml','Lab/Pickle','Lab/logic'],
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
       install_requires=[
    'toml==0.10.2',
    'PyYAML == 5.3.1',
    'simplejson == 3.16.0'],
     entry_points ={
       'console_scripts': [
                'Lab = Lab.Parser:main'
            ]
        },
)
