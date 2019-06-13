from setuptools import setup, find_packages

with open("README.md") as f:
    long_desc = f.read()

setup( name='delegate',
       version='0.1.0',
       author='D. Scott Boggs',
       author_email='scott@tams.tech',
       description="delegate attributes of a class to another attribute's properties",
       long_description=long_desc,
       long_description_content_type='text/markdown',
       packages=find_packages(),
       url='https://github.com/dscottboggs/python-delegate',
       classifiers=[
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: MIT License',
           'Programming Language :: Python',
           'Topic :: Software Development :: Libraries :: Python Modules',
           'Topic :: Software Development :: Code Generators'
       ]
)
