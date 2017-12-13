# encoding:utf-8
import sys
from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

compile_args = []
extra_link_args = []

package_data = ["ctp/*.xml", "ctp/*.dtd"]

if sys.platform == "linux":
    package_data.append("ctp/*.so")
elif sys.platform == "win32":
    package_data.append("ctp/*.dll")

# if sys.platform == "linux":
#     compile_args = ["-03", "-Wall"]
#     extra_link_args = ["-g"]
#
# elif sys.platform == "win32":
#     compile_args = ["/GR", "/EHsc"]
#     extra_link_args = []
#

# common_args = {
#     "include_dirs": [ctp_dir, header_dir],
#     "library_dirs": [ctp_dir],
#     "language": "c++"
# }

ext_modules = [
    Extension("demo",
              sources=["demo.pyx"],
              libraries=["m"]  # Unix-like specific
              )
]

setup(name="python CTP api",
      version="6.3.6",
      author="winton.wang",
      author_email="winton@quant.vc",
      description="This is CTP wrapper python interface",
      include_package_data=True,
      package_data={"": package_data},
      ext_modules=cythonize(ext_modules)
      )
