#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Leandro
#
# Created:     08/02/2014
# Copyright:   (c) Leandro 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from os import *
from random import *
from rabin import fatoracao, inverso



p = 45343
q = 7243
e = 220037467
d = inverso(e, (p-1)*(q-1))
N = 76010536
print(d)

M = (N**d) % (p*q)


