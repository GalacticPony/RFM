from setuptools import setup 

def readme():
    with open ('README.rst') as f:
        return f.read()

setup(name='myRFMpackage',
      description='What the package does', 
      version='1.0', 
      py_modules=['calculateRFM'], 
      zip_safe=False, 
      install_requires=['pandas','numpy'], 
      packages=['myRFMpackage'])