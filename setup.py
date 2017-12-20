# encoding:utf-8
import codecs
import os
import re
import sys

from setuptools import setup, find_packages

from Cython.Build import cythonize
from Cython.Distutils import build_ext, Extension


def find_version(*file_paths):
    """
    Don't pull version by importing package as it will be broken due to as-yet uninstalled
    dependencies, following recommendations at  https://packaging.python.org/single_source_version,
    extract directly from the init file
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r', encoding="utf-8") as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


package_data = ["*.xml", "*.dtd"]
project_dir = os.path.join(os.path.dirname(__file__), "ctpwrapper")
ctp_dir = os.path.join(project_dir, "ctp")
cython_headers = os.path.join(project_dir, "headers")

extra_link_args = None
extra_compile_args = None

if sys.platform == "linux":
    package_data.append("*.so")
    extra_compile_args = ["-Wall"]  # "-03",
    extra_link_args = ["-g"]

elif sys.platform == "win32":
    extra_compile_args = ["/GR", "/EHsc"]
    # extra_link_args = []
    package_data.append("*.dll")

# extensions = [
#     Extension(name="ltsapi.MdApi",
#               sources=["ltsapi/MdApi.pyx"],
#               extra_compile_args=compile_args,
#               extra_objects=["securitymduserapi.lib"] if sys.platform == "win32" else None,
#               extra_link_args=extra_link_args,
#               libraries=["securitymduserapi"],
#               **common_args),


common_args = {
    "cython_include_dirs": [cython_headers],
    "include_dirs": [ctp_dir],
    "library_dirs": [ctp_dir],
    "language": "c++"
}

ext_modules = [
    Extension(name="ctpwrapper.MdApi",
              sources=["ctpwrapper/MdApi.pyx"],
              libraries=["thostmduserapi"],
              extra_compile_args=extra_compile_args,
              extra_link_args=extra_link_args,
              **common_args),
]

setup(
    name="ctpwrapper",
    version=find_version("ctpwrapper", "__init__.py"),
    setup_requires=["cython"],
    install_requires=["cython"],
    packages=find_packages(),
    include_dirs=[ctp_dir],
    include_package_data=True,
    platforms=["win32", "linux"],
    package_data={"": package_data},
    ext_modules=cythonize(ext_modules),
    cmdclass={'build_ext': build_ext},
)
