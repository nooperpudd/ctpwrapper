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
__version__ = "6.6.1"
__date__ = "2021-04-06"

from ctpwrapper.Md import MdApiPy
from ctpwrapper.Trader import TraderApiPy


__all__ = (
    "MdApiPy",
    "TraderApiPy"
)

from .datacollect import GetSystemInfo
