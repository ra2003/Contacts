#  __init__.py: The package
#  Copyright (C) 2020  Delvian Valentine <delvian.valentine@gmail.com>
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

"""Store your contacts."""

__author__ = 'Delvian Valentine <delvian.valentine@gmail.com>'
__version__ = '2.0b1'

import os.path

# Store the contacts in a temporary file while developing the app.
DEV_MODE = False
PATH = os.path.expanduser(os.path.join('~', '.contacts'))
CONTACTS_FILE = '.contacts' if DEV_MODE else PATH
COPYRIGHT = f'''Copyright (C) 2020  {__author__}
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under
certain conditions.  See the GNU General Public License for more
details <https://www.gnu.org/licenses/>.'''