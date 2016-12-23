from setuptools import setup, find_packages

setup (
       name='CipherDecryptor',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=[],
       entry_points={
         'console_scripts': [
             'my_project = my_project.__main__:main'
         ]
       },
       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='lamp',
       author_email='',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )