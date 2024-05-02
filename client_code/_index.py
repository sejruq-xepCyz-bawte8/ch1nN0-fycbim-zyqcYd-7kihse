from anvil.js.window import performance
from time import time
from anvil import *

tp = performance.timeOrigin
t0 = time()
open_form('About', t0)

lapp = t0-tp/1000
print("module after open", lapp)