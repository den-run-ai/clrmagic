from setuptools import setup
from distutils.command.build_ext import build_ext
import sys

full_info = open("README.md").read()

class clrmagic_build_ext(build_ext):
    def build_extension(self, ext):
        """
        build clrmagic.dll using csc or mcs
        """
        _clr_compiler = "csc" if sys.platform == "win32" else "mcs"
        cmd = [ 
            _clr_compiler,
            "clrmagic.cs",
            "/target:library"
        ]
        check_call(" ".join(cmd), shell=True)    

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
        "Development Status :: 3 - Alpha"
        "Environment :: Web Environment",
        "Framework :: IPython",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft",
        "Programming Language :: C#",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development"
    ],
    zip_safe = False,
    data_files = [
        ("{install_platlib}", ["{build_lib}/clrmagic.dll"]),
    cmdclass = {
        "build_ext": clrmagic_build_ext
    }
)
    
    
