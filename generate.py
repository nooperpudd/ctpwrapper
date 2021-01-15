# encoding:utf-8
import codecs
import os
import re
from collections import OrderedDict

CTP_PATH = os.path.join(os.path.dirname(__file__), "ctp")

HEADER_PATH = os.path.join(CTP_PATH, "header")

USERAPI_DATA_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiDataType.h")
USERAPI_STRUCT_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiStruct.h")

GENERATE_PATH = os.path.join(os.path.dirname(__file__), "ctpwrapper/headers")


def generate_structure(datatype_dict):
    """
    generate structure file
    :return:
    """

    generate_file = os.path.join(GENERATE_PATH, "ThostFtdcUserApiStruct.pxd")

    data_struct_file = codecs.open(generate_file, "w", encoding="utf-8")
    data_struct_file.write("# encoding:utf-8")
    data_struct_file.write("\n" * 2)

    data_struct_file.write("from .ThostFtdcUserApiDataType cimport *\n")
    data_struct_file.write("\n" * 2)

    data_struct_file.write("cdef extern from 'ThostFtdcUserApiStruct.h':\n")

    for line in codecs.open(USERAPI_STRUCT_FILE, encoding="utf-8"):
        if line.startswith("struct"):
            result = re.findall("\w+", line)
            name = result[1]
            data_struct_file.write("    cdef struct {name}:\n".format(name=name))
        else:

            result = re.findall("\w+", line)

            if result:
                type_name = result[0]
                if type_name in datatype_dict:
                    data_struct_file.write("    " + line.replace(";", ""))

    data_struct_file.close()


def generate_datatype():
    """
    generate structure data
    :return:
    """
    datatype_dict = OrderedDict()

    generate_file = os.path.join(GENERATE_PATH, "ThostFtdcUserApiDataType.pxd")
    data_type_file = codecs.open(generate_file, "w", encoding="utf-8")

    data_type_file.write("# encoding:utf-8")
    data_type_file.write("\n" * 2)
    data_type_file.write("cdef extern from 'ThostFtdcUserApiDataType.h':\n")

    for line in codecs.open(USERAPI_DATA_FILE, encoding="utf-8"):
        if line.startswith("enum"):
            # special output data
            data_type_file.write(""" 
    cdef enum THOST_TE_RESUME_TYPE:
        THOST_TERT_RESTART = 0
        THOST_TERT_RESUME
        THOST_TERT_QUICK
        THOST_TERT_NONE
""")
            # special write data
        if line.startswith("#define"):
            pass
        elif line.startswith("typedef"):
            result = re.findall("\w+", line)

            _type = result[1]
            name = result[2]
            datatype_dict.setdefault(name)
            length = None

            if len(result) == 4:  # char xxxxx [10]
                length = result[3]

            if length:
                data_type_file.write("    ctypedef {_type} {name}[{length}]\n".format(_type=_type,
                                                                                       name=name,
                                                                                       length=length))
            else:
                data_type_file.write("    ctypedef {_type} {name}\n".format(_type=_type,
                                                                             name=name))
    data_type_file.close()
    return datatype_dict


if __name__ == "__main__":
    datatype_dict = generate_datatype()
    generate_structure(datatype_dict)
