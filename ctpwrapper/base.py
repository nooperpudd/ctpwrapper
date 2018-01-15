# encoding:utf-8
import ctypes


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
                results[key] = _value.decode("gbk")
            else:
                results[key] = _value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = ["%s:%s" % (item, getattr(self, item)) for item, value in self._fields_]
        return "%s<%s>" % (self.__class__.__name__, ",".join(items))