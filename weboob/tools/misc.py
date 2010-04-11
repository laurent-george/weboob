# -*- coding: utf-8 -*-

"""
Copyright(C) 2010  Romain Bignon

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

"""

from dateutil import tz

def toUnicode(text):
    r"""
    >>> toUnicode('ascii')
    u'ascii'
    >>> toUnicode(u'utf\xe9'.encode('UTF-8'))
    u'utf\xe9'
    >>> toUnicode(u'unicode')
    u'unicode'
    """
    if isinstance(text, unicode):
        return text
    if not isinstance(text, str):
        text = str(text)
    try:
        return unicode(text, "utf8")
    except UnicodeError:
        pass
    return unicode(text, "ISO-8859-1")

def local2utc(d):
    d = d.replace(tzinfo=tz.tzlocal())
    d = d.astimezone(tz.tzutc())
    return d

try:
    from html2text import html2text
except ImportError:
    def html2text(s):
        return s
