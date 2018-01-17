# encoding=utf-8
import codecs
import os
import re
from collections import OrderedDict

CTP_PATH = os.path.join(os.path.dirname(__file__), "ctp")
HEADER_PATH = os.path.join(CTP_PATH, "header")
USERAPI_DATA_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiDataType.h")
USERAPI_STRUCT_FILE = os.path.join(HEADER_PATH, "ThostFtdcUserApiStruct.h")
GENERATE_FILE = os.path.join(os.path.dirname(__file__), "ctpwrapper/ApiStructure.py")


class Parse(object):
    """
    解析结构体
    """

    def __init__(self, type_file, struct_file):
        """
        :param type_file:
        :param struct_file:
        """
        self.type_file = type_file
        self.struct_file = struct_file

        self.data_type = OrderedDict()
        self.struct = OrderedDict()

    def parse_datatype(self):
        """
        处理 UserApiDataType file.
        """
        for line in codecs.open(self.type_file, encoding="utf-8"):
            if line.startswith("typedef"):

                result = re.findall("\w+", line)
                name = result[2]
                type_ = result[1]

                if len(result) == 4 and type_ == "char":
                    self.data_type[name] = {
                        "type": "str",
                        "length": int(result[3])
                    }
                elif type_ == "char":
                    self.data_type[name] = {
                        "type": "str",
                    }
                else:
                    self.data_type[name] = {
                        "type": type_,
                    }

    def parse_struct(self):
        """
        解析结构体定义
        """
        self.parse_datatype()

        for line in codecs.open(self.struct_file, encoding="utf-8"):
            # name = None

            if line.startswith("struct"):
                result = re.findall("\w+", line)
                name = result[1]  # assign the name

                self.struct[name] = OrderedDict()

            if line.strip().startswith("TThostFtdc"):
                result = re.findall("\w+", line)
                field_type = result[0]
                field_name = result[1].replace(";", "")
                self.struct[name][field_name] = self.data_type[field_type]


def generate_struct(struct, py_file):
    for item in struct:
        py_file.write("class {class_name}(Base):\n".format(class_name=item.replace("CThostFtdc", "")))

        py_file.write("    _fields_ = [\n")

        for field in struct[item]:
            field_data = struct[item][field]
            if field_data["type"] == "double":
                py_file.write("        ('{field}', ctypes.c_double),\n".format(field=field))
            elif field_data["type"] == "int":
                py_file.write("        ('{field}', ctypes.c_int),\n".format(field=field))
            elif field_data["type"] == "short":
                py_file.write("        ('{field}', ctypes.c_short),\n".format(field=field))
            elif field_data["type"] == "str" and "length" not in field_data:
                py_file.write("        ('{field}', ctypes.c_char),\n".format(field=field))
            elif field_data["type"] == "str" and "length" in field_data:
                py_file.write("        ('{field}', ctypes.c_char*{length}),\n".format(field=field,
                                                                                      length=field_data["length"]))

        py_file.write("    ]\n")

        py_file.write("    def __init__(self,%s):\n" % ",".join(["%s=''" % field for field in struct[item]]))
        py_file.write("        super({class_name},self).__init__()\n".format(class_name=item.replace("CThostFtdc", "")))

        for field in struct[item]:
            if struct[item][field]["type"] == "double":
                py_file.write("        self.%s=float(%s)\n" % (field, field))
            if struct[item][field]["type"] in ["int", "short"]:
                py_file.write("        self.%s=int(%s)\n" % (field, field))
            if struct[item][field]["type"] == "str":
                py_file.write("        self.%s=self._to_bytes(%s)\n" % (field, field))


def generate_interface():
    parse = Parse(USERAPI_DATA_FILE, USERAPI_STRUCT_FILE)
    parse.parse_struct()
    structure = parse.struct

    # generate python
    py_file = codecs.open(GENERATE_FILE, "w")

    py_file.write('# encoding=utf-8\n')
    py_file.write("import ctypes\n")
    py_file.write("from ctpwrapper.base import Base\n")
    py_file.write("\n" * 2)

    generate_struct(structure, py_file)

    py_file.close()


if __name__ == "__main__":
    generate_interface()
