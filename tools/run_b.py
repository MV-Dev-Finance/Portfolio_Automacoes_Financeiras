import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from kit import render_all
from screens_a import SCREENS_A
from screens_b import SCREENS_B
out=os.path.join(os.path.dirname(__file__),'..','assets','screens')
render_all({**SCREENS_A, **SCREENS_B},out)
print(len(SCREENS_A)+len(SCREENS_B))
