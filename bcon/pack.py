#
#  Bcon
#  Python Binary Compressed Object Notation module.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""
Packs any of the following types into a string of bytes:
- None (\x00)
- Bool (\x01)
- Int (\x02)
- Float (\x03)
- String (\x04)
- Bytes (\x05)
- Tuple (\x06), may only contain these types.
- List (\x07), may only contain these types.
- Dict (\x08), may only contain these types.
"""

import struct
import io
from typing import Any, Dict, List, Tuple, Union


def pack(obj: Any):
    if obj is None:
        data = b"\x00"
    elif isinstance(obj, bool):
        data = b"\x01"
        data += b"\x01" if obj else b"\x00"
    elif isinstance(obj, int):
        data = b"\x02"
        data += b"\x00" if obj > 0 else b"\x01"
        data += struct.pack("<I", abs(obj))
        if len(data) != 6:
            raise ValueError(f"Integer {obj} is too large or too small.")
    elif isinstance(obj, float):
        data = b"\x03" + struct.pack("f", obj)
        if len(data) != 5:
            raise ValueError(f"Float {obj} is too large or too small.")
    else:
        raise TypeError(f"Type {obj.__class__.__name__} is not allowed.")

    return data


def unpack(data: Union[bytes, io.BytesIO]):
    if isinstance(data, bytes):
        data = io.BytesIO(data)

    cls = data.read(1)
    if cls == b"\x00":
        obj = None
    elif cls == b"\x01":
        obj = (data.read(1) == b"\x01")

    return obj
