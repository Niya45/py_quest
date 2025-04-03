# MODULES : files containing code to be included in a program
# useful to break down programs into reusable files

# "import" : import built in or custom modules
# EG: math, time, ranodm etc.

# built in modules :
# print(help("modules"))

# as : give the module a unique name specific to this file
import math as mathematics
print(mathematics.pi)

# import something from a module
from math import pi
print(pi)
# importing the module compleatly is recommended : names can be confused, what if var named pi exists?

## IMPORT A CUSTOM MODULES

import random_module # or path/to/file

