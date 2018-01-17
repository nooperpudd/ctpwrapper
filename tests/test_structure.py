# encoding:utf-8

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

        self.assertEqual(field.BrokerID, b"45544")
        self.assertEqual(field.FromCurrencyID, b"4343")
        self.assertEqual(field.FromCurrencyUnit, 19.0)
        self.assertEqual(field.ToCurrencyID, b"4334")
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
        
        self.assertEqual(field.BrokerID, b"45544")
        self.assertEqual(field.FromCurrencyID, b"4343")
        self.assertEqual(field.FromCurrencyUnit, 0.0)
        self.assertEqual(field.ToCurrencyID, b"")
        self.assertEqual(field.ExchangeRate, 11.0)
