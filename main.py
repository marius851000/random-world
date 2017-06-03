from graphic import *

import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

GUI=graphic()

sys.stdout = orig_stdout
f.close()