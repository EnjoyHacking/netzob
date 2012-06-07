# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+
#| Standard library imports
#+---------------------------------------------------------------------------+
import logging
import base64

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.Type.TypeConvertor import TypeConvertor
from netzob.Common.Filters.MathematicFilter import MathematicFilter


#+---------------------------------------------------------------------------+
#| Base64Filter:
#|     Definition of a base64 transformation filter
#+---------------------------------------------------------------------------+
class Base64Filter(MathematicFilter):

    TYPE = "FormatFilter"

    def __init__(self, name):
        MathematicFilter.__init__(self, Base64Filter.TYPE, name)

    def apply(self, message):
        result = message
        try:
            rawContent = TypeConvertor.netzobRawToPythonRaw(message)
            b64Content = base64.b64decode(rawContent)
            result = TypeConvertor.pythonRawToNetzobRaw(b64Content)
        except TypeError as error:
            logging.warning("Impossible to compute the base64 value of message (error={0})".format(str(error)))
            result = ""
        return result
