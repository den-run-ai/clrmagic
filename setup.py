from setuptools import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.command.install_data import install_data
import sys
import os
from subprocess import check_call

#full_info = open("README.md").read()

class clrmagic_build_ext(build_ext):
    def build_extension(self, ext):
        """
        build clrmagic.dll using csc or mcs
        """
        if sys.platform == "win32":
            _clr_compiler = "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\csc.exe"
        else:
            _clr_compiler = "mcs"
        cmd = [ 
            _clr_compiler,
            "/target:library",
            "clrmagic.cs"
        ]
        check_call(" ".join(cmd), shell=True)    

class clrmagic_install_data(install_data):
    def run(self):
        build_cmd = self.get_finalized_command("build_ext")
        install_cmd = self.get_finalized_command("install")
        build_lib = os.path.abspath(build_cmd.build_lib)
        install_platlib = os.path.relpath(install_cmd.install_platlib, self.install_dir)

        for i, data_files in enumerate(self.data_files):
            if isinstance(data_files, str):
                self.data_files[i] = data_files[i].format(build_lib=build_lib)
            else:
                for j, filename in enumerate(data_files[1]):
                    data_files[1][j] = filename.format(build_lib=build_lib)
                dest = data_files[0].format(install_platlib=install_platlib)
                self.data_files[i] = dest, data_files[1]

        return install_data.run(self)

setupdir = os.path.dirname(__file__)
if setupdir:
    os.chdir(setupdir)

setup(
    name = "clrmagic",
    version = "0.0.1a2",
    description = "IPython cell magic to use .NET languages",
    author = "Xavier Dupré, Denis Akhiyarov",
    author_email = "denis.akhiyarov@gmail.com",
    url = "https://github.com/denfromufa/clrmagic",
    license = "MIT",
    keywords = ".NET CLR Mono Jupyter IPython notebook C# CSHARP pythonnet",
    py_modules = ["clrmagic"],
    install_requires = ["pythonnet"],
    classifiers = [
        "Development Status :: 3 - Alpha",
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
    ext_modules=[
            Extension("clrmagic", sources=["clrmagic.cs"])
    ],
    data_files = [
        ("{install_platlib}", ["clrmagic.dll"])
    ],
    cmdclass = {
        "build_ext": clrmagic_build_ext,
        "install_data": clrmagic_install_data
    }
)
