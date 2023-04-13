import os, platform

os.system('git pull')

 

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from YEAR208064 import approval

    crackfile()

elif bit == '32bit':

    from YEAR2080 import approval

    crackfile()
