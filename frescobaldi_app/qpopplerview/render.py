# This file is part of the qpopplerview package.
#
# Copyright (c) 2010, 2011 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.


"""
Rendering Poppler (PDF) documents helper stuff.
"""


class RenderOptions(object):
    """Manages rendering options."""
    def __init__(self):
        self._renderHint = None
        self._paperColor = None
    
    def read(self, document):
        """Reads rendering options from the given Poppler.Document."""
        self._renderHint = document.renderHints()
        self._paperColor = document.paperColor()
        
    def write(self, document):
        """Writes our rendering options to the given Poppler.Document."""
        if self._renderHint is not None:
            document.setRenderHint(self._renderHint)
        
        if self._paperColor is not None:
            document.setPaperColor(self._paperColor)
        
    def setRenderHint(self, hint):
        """Sets the Poppler.Document.RenderHints. Use None to unset."""
        self._renderHint = hint
    
    def renderHint(self):
        """Returns the currently set RenderHint(s)."""
        return self._renderHint
        
    def setPaperColor(self, color):
        """Sets the paper color for rendering. Use None to unset."""
        self._paperColor = color
        
    def paperColor(self):
        """Returns the currently set paper color."""
        return self._paperColor

