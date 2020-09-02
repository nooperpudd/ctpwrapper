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

import unittest

from ctpwrapper import ApiStructure


class TestStructure(unittest.TestCase):
    # ('BrokerID', ctypes.c_char * 11),
    # ('FromCurrencyID', ctypes.c_char * 4),
    # ('FromCurrencyUnit', ctypes.c_double),
    # ('ToCurrencyID', ctypes.c_char * 4),
    # ('ExchangeRate', ctypes.c_double),

    def test_to_dict(self):
        result = {
            "BrokerID": "45544",
            "FromCurrencyID": "4343",
            "FromCurrencyUnit": 19.0,
            "ToCurrencyID": "4334",
            "ExchangeRate": 11.0
        }
        field = ApiStructure.ExchangeRateField(
            BrokerID="45544",
            FromCurrencyID="4343",
            FromCurrencyUnit=19.0,
            ToCurrencyID="4334",
            ExchangeRate=11.0
        )
        result_dict = field.to_dict()
        self.assertDictEqual(result, result_dict)

    def test_from_dict(self):
        result = {
            "BrokerID": "45544",
            "FromCurrencyID": "4343",
            "FromCurrencyUnit": 19.0,
            "ToCurrencyID": "4334",
            "ExchangeRate": 11.0
        }
        field = ApiStructure.ExchangeRateField.from_dict(result)

        self.assertEqual(field.BrokerID, "45544")
        self.assertEqual(field.FromCurrencyID, "4343")
        self.assertEqual(field.FromCurrencyUnit, 19.0)
        self.assertEqual(field.ToCurrencyID, "4334")
        self.assertEqual(field.ExchangeRate, 11.0)

    def test_struct_missing_parameter(self):
        result = {
            "BrokerID": "45544",
            "FromCurrencyID": "",
            "FromCurrencyUnit": 0.0,
            "ToCurrencyID": "4334",
            "ExchangeRate": 11.0
        }

        field = ApiStructure.ExchangeRateField(
            BrokerID="45544",
            ToCurrencyID="4334",
            ExchangeRate=11.0
        )
        result_dict = field.to_dict()
        self.assertDictEqual(result_dict, result)

    def test_dict_missing_parameter(self):
        result = {
            "BrokerID": "45544",

            "ToCurrencyID": "4334",
            "ExchangeRate": 11.0
        }
        field = ApiStructure.ExchangeRateField.from_dict(result)

        self.assertEqual(field.BrokerID, "45544")
        self.assertEqual(field.FromCurrencyID, "")
        self.assertEqual(field.FromCurrencyUnit, 0.0)
        self.assertEqual(field.ToCurrencyID, "4334")
        self.assertEqual(field.ExchangeRate, 11.0)
