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


import socket
import urllib.parse
from contextlib import closing


def check_address_port(tcp):
    """
    :param tcp:
    :return:
    """
    host_schema = urllib.parse.urlparse(tcp)

    ip = host_schema.hostname
    port = host_schema.port

    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((ip, port)) == 0:
            return True  # OPEN
        else:
            return False  # closed
