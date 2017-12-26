# encoding:utf-8

import ctypes

import json


class Base(ctypes.Structure):

    def _to_bytes(self, value):
        """
        :return:
        """
        if isinstance(value, bytes):
            return value
        else:
            return bytes(value, encoding="utf-8")

    @classmethod
    def from_dict(cls, obj):
        """
        :return:
        """
        return cls(**obj)

    def to_dict(self):
        """
        :return:
        """
        results = {}
        for key, value in self._fields_:
            _value = getattr(self, key)
            if isinstance(_value, bytes):
                results[key] = _value.decode()
            else:
                results[key] = _value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = ["%s:%s" % (item, getattr(self, item)) for item, value in self._fields_]
        return "%s<%s>" % (self.__class__.__name__, ",".join(items))


class D(Base):
    _fields_ = [("hello", ctypes.c_double),
                ("nihao", ctypes.c_char_p)]

    def __init__(self, hello="", nihao=""):
        super(D, self).__init__()
        self.hello = float(hello)
        # a=
        self.nihao = self._to_bytes(nihao)


gg = {"hello": "1"}
dd = D.from_dict(gg)
print(dd)
print(dd.to_dict())

d = D(hello=1, nihao="a")
print(d.to_dict())
e = json.dumps(d.to_dict())
print(d)
print(e)
