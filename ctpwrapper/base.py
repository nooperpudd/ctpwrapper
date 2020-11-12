# encoding:utf-8
"""
(Copyright) 2018, Winton Wang <365504029@qq.com>

ctpwrapper is free software: you can redistribute it and/or modify
it under the terms of the GNU LGPLv3 as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ctpwrapper.  If not, see <http://www.gnu.org/licenses/>.

"""
import ctypes
import typing


class Base(ctypes.Structure):

    def __getattribute__(self, item):
        value = super().__getattribute__(item)
        if isinstance(value, bytes):
            return value.decode("gbk")
        else:
            return value

    def _to_bytes(self, value):
        """
        :return:
        """
        if isinstance(value, bytes):
            return value
        else:
            return bytes(str(value), encoding="utf-8")

    @classmethod
    def from_dict(cls, obj: typing.Dict):
        """
        :return:
        """
        return cls(**obj)

    def to_dict(self) -> typing.Dict:
        """
        :return:
        """
        results = {}
        for key, _ in self._fields_:
            _value = getattr(self, key)
            results[key] = _value
        return results

    def __repr__(self):
        """
        :return:
        """
        items = ["{0}({1})".format(item, getattr(self, item)) for item, value in self._fields_]
        return "{0}<{1}>".format(self.__class__.__name__, ",".join(items))
