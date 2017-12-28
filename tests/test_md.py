# encoding:utf-8

from ctpwrapper.Md import MdApiPy

import unittest


class MdTest(unittest.TestCase):

    def test_get_version(self):
        print(MdApiPy.GetApiVersion())