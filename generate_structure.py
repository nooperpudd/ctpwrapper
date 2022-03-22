# encoding=utf-8
import codecs
import linecache
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
        self.struct_doc = dict()  # for struct doc

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

        for index, line in enumerate(codecs.open(self.struct_file,
                                                 encoding="utf-8")):
            doc_line = index

            if line.startswith("struct"):
                result = re.findall("\w+", line)
                name = result[1]  # assign the name
                self.struct[name] = OrderedDict()

                # stuct doc
                struct_doc = linecache.getline(self.struct_file, doc_line)
                struct_doc = struct_doc.strip().replace("///", "")
                self.struct_doc[name] = struct_doc

            if line.strip().startswith("TThostFtdc"):
                result = re.findall("\w+", line)
                field_type = result[0]
                field_name = result[1].replace(";", "")
                struct_dict = self.struct[name]
                struct_dict[field_name] = self.data_type[field_type]

                # doc
                field_doc = linecache.getline(self.struct_file, doc_line)
                field_doc = field_doc.strip().replace("///", "")
                struct_dict[field_name + "_doc"] = field_doc


def generate_struct(struct, struct_doc, py_file):
    for item in struct:

        py_file.write("class {class_name}(Base):\n".format(class_name=item.replace("CThostFtdc", "")))
        py_file.write('    """{doc}"""\n'.format(doc=struct_doc[item]))
        py_file.write("    _fields_ = [\n")
        struct_dict = struct[item]

        for field in struct_dict:

            if field.endswith("_doc"):
                continue
            field_data = struct_dict[field]
            field_doc = struct[item][field+"_doc"]

            if field_data["type"] == "double":
                py_file.write("        ('{field}', ctypes.c_double),  # {doc}\n".format(field=field, doc=field_doc))
            elif field_data["type"] == "int":
                py_file.write("        ('{field}', ctypes.c_int),  # {doc}\n".format(field=field, doc=field_doc))
            elif field_data["type"] == "short":
                py_file.write("        ('{field}', ctypes.c_short),  # {doc}\n".format(field=field, doc=field_doc))
            elif field_data["type"] == "str" and "length" not in field_data:
                py_file.write("        ('{field}', ctypes.c_char),  # {doc} \n ".format(field=field, doc=field_doc))
            elif field_data["type"] == "str" and "length" in field_data:
                py_file.write("        ('{field}', ctypes.c_char*{len}),  # {doc}\n".format(field=field,
                                                                                           len=field_data["length"],
                                                                                           doc=field_doc))

        py_file.write("    ]\n")

        struct_fields = []
        for field in struct_dict:

            if field.endswith("_doc"):
                continue

            field_data = struct_dict[field]
            if field_data["type"] == "double":
                struct_fields.append("%s:float=0.0" % field)
            elif field_data["type"] in ["int", "short"]:
                struct_fields.append("%s:int=0" % field)
            else:
                struct_fields.append("%s:str=''" % field)
        py_file.write("    def __init__(self,%s):\n" % ",".join(struct_fields))
        py_file.write("        super({class_name},self).__init__()\n".format(class_name=item.replace("CThostFtdc", "")))

        for field in struct_dict:
            if field.endswith("_doc"):
                continue
            if struct_dict[field]["type"] == "double":
                py_file.write("        self.%s=float(%s)\n" % (field, field))
            if struct_dict[field]["type"] in ["int", "short"]:
                py_file.write("        self.%s=int(%s)\n" % (field, field))
            if struct_dict[field]["type"] == "str":
                py_file.write("        self.%s=self._to_bytes(%s)\n" % (field, field))


def generate_interface():
    parse = Parse(USERAPI_DATA_FILE, USERAPI_STRUCT_FILE)
    parse.parse_struct()
    structure = parse.struct
    struct_doc = parse.struct_doc
    # generate python
    py_file = codecs.open(GENERATE_FILE, "w", encoding="utf-8")

    py_file.write('# encoding=utf-8\n')
    py_file.write("import ctypes\n")
    py_file.write("from ctpwrapper.base import Base\n")
    py_file.write("\n" * 2)

    generate_struct(structure, struct_doc, py_file)

    py_file.close()


if __name__ == "__main__":
    generate_interface()
