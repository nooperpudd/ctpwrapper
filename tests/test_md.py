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

from ctpwrapper.Md import MdApiPy
import pytest
import unittest
# import server_check
#
# tcp = "tcp://180.168.146.187:10011"
#
# @pytest.mark.skipif(server_check.check_address_port(tcp),
#                     reason="180.168.146.187:10011 server can't establish")
class MdTest(unittest.TestCase):
    def test_get_version(self):
        print(MdApiPy.GetApiVersion())
# 
#     def setUp(self):
#         self.investor_id = "089303"
#         self.broker_id = "9999"
#         self.password = "198759"
#         self.md = MdApiPy()
#         self.md.RegisterNameServer(tcp)
#
#     def test_login(self):
#
#         self.md.ReqUserLogin()
#     def test_req_market_data(self):
#         pass