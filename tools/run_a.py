import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from kit import render_all
from screens_a import SCREENS_A
out=os.path.join(os.path.dirname(__file__),'..','assets','screens')
render_all(SCREENS_A,out)
print(len(SCREENS_A))
