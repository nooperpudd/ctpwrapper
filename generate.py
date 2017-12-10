# encoding:utf-8
import codecs
import os
import re

CTP_PATH = os.path.join(os.path.dirname(__file__), "ctp")

HEADER_PATH = os.path.join(CTP_PATH, "header")

USERAPI_DATA_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiDataType.h")
USERAPI_STRUCT_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiStruct.h")

GENERATE_PATH = os.path.join(os.path.dirname(__file__), "ctpwrapper")



def generate_structure():
    """
    generate structure file
    :return:
    """
    for line in codecs.open(USERAPI_STRUCT_FILE, encoding="utf-8"):
        if line.startswith("struct"):
            pass
            # for line in file.readline():


def generate_datatype():
    """
    generate structure data
    :return:
    """
    generate_file = os.path.join(GENERATE_PATH, "ThostFtdcUserApiDataType.pxd")
    data_type_file = codecs.open(generate_file, "w", encoding="utf-8")

    data_type_file.write("# encoding:utf-8")
    data_type_file.write("\n" * 2)
    data_type_file.write("cdef  extern  from './ctp/ThostFtdcUserApiDataType.h': \n")

    for line in codecs.open(USERAPI_DATA_FILE, encoding="utf-8"):
        if line.startswith("enum"):
            pass
        if line.startswith("#define"):
            pass
        elif line.startswith("typedef"):
            result = re.findall("\w+", line)

            _type = result[1]
            name = result[2]
            length = None

            if len(result) == 4:  # char xxxxx [10]
                length = result[3]

            if length:
                data_type_file.write("    ctypedef {_type}[{length}] {name} \n".format(_type=_type,
                                                                                       name=name,
                                                                                       length=length))
            else:
                data_type_file.write("    ctypedef {_type} {name} \n".format(_type=_type,
                                                                             name=name))
    data_type_file.close()


if __name__ == "__main__":
    generate_datatype()
    generate_structure()
