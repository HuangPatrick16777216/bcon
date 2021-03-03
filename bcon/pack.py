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

