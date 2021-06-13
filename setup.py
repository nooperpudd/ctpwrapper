# encoding:utf-8
import codecs
import os
import platform
import re
import shutil
import sys
from distutils.dir_util import copy_tree
from setuptools import setup

from Cython.Build import cythonize, build_ext
from Cython.Distutils import Extension as Cython_Extension


# issue put in the cython library bellow will cause
# error: each element of 'ext_modules' option must be an Extension instance or 2-tuple


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


if platform.architecture()[0] != "64bit":
    raise EnvironmentError("Please install Python x86-64")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(base_dir, "ctpwrapper")
ctp_dir = os.path.join(base_dir, "ctp")
cython_headers = os.path.join(project_dir, "headers")
header_dir = os.path.join(ctp_dir, "header")
cpp_header_dir = os.path.join(project_dir, "cppheader")

lib_dir = None
package_data = ["*.xml", "*.dtd"]
extra_link_args = None
extra_compile_args = None

if sys.platform == "linux":
    lib_dir = os.path.join(ctp_dir, "linux")
    package_data.append("*.so")
    extra_compile_args = ["-Wall"]
    extra_link_args = ['-Wl,-rpath,$ORIGIN']

elif sys.platform == "win32":
    lib_dir = os.path.join(ctp_dir, "win")
    extra_compile_args = ["/GR", "/EHsc"]
    # extra_link_args = []
    package_data.append("*.dll")

package_data.append("error.dtd")
package_data.append("error.xml")
shutil.copy2(header_dir + "/error.dtd", project_dir + "/error.dtd")
shutil.copy2(header_dir + "/error.xml", project_dir + "/error.xml")

if sys.platform in ["linux", "win32"]:
    copy_tree(lib_dir, project_dir)

common_args = {
    "cython_include_dirs": [cython_headers],
    "include_dirs": [header_dir, cpp_header_dir],
    "library_dirs": [lib_dir],
    "language": "c++",
    "extra_compile_args": extra_compile_args,
    "extra_link_args": extra_link_args,
}

ext_modules = [
    Cython_Extension(name="ctpwrapper.MdApi",
                     sources=["ctpwrapper/MdApi.pyx"],
                     libraries=["thostmduserapi_se"],
                     **common_args),
    Cython_Extension(name="ctpwrapper.TraderApi",
                     sources=["ctpwrapper/TraderApi.pyx"],
                     libraries=["thosttraderapi_se"],
                     **common_args),
    Cython_Extension(name="ctpwrapper.datacollect",
                     sources=["ctpwrapper/datacollect.pyx"],
                     libraries=["LinuxDataCollect"] if sys.platform == "linux" else ["WinDataCollect"],
                     **common_args)
]

setup(
    name="ctpwrapper",
    version=find_version("ctpwrapper", "__init__.py"),
    description="CTP client v6.3.19",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    license="LGPLv3",
    keywords="CTP,Future,SHFE,Shanghai Future Exchange",
    author="Winton Wang",
    author_email="365504029@qq.com",
    url="https://github.com/nooperpudd/ctpwrapper",
    include_dirs=[header_dir, cpp_header_dir],
    platforms=["win32", "linux"],
    packages=["ctpwrapper"],
    package_data={"": package_data},
    python_requires=">=3.6",
    # cython: binding=True
    # binding = true for inspect get callargs
    ext_modules=cythonize(ext_modules,
                          compiler_directives={'language_level': 3,
                                               "binding": True}
                          ),
    cmdclass={'build_ext': build_ext},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries"
    ]
)
