from setuptools import setup

full_info = open("README.md").read()

setup(
    name = "clrmagic",
    version = "0.0.1",
    description = "IPython cell magic to use .NET languages",
    author = "Xavier Dupré, Denis Akhiyarov",
    author_email = "denis.akhiyarov@gmail.com",
    url = "https://github.com/denfromufa/clrmagic",
    license = "MIT",
    keywords = ".NET CLR Mono Jupyter IPython notebook C# CSHARP pythonnet",
    pymodules = ["clrmagic"],
    install_requires = ["pythonnet"],
    classifiers = [
        Development Status :: 3 - Alpha
        Environment :: Web Environment
        Framework :: IPython
        Intended Audience :: Science/Research
        License :: OSI Approved :: MIT License
        Operating System :: Microsoft
        Programming Language :: C#
        Programming Language :: Python
        Programming Language :: Python :: Implementation :: CPython
        Topic :: Scientific/Engineering
        Topic :: Software Development
    ]
)
    
    
