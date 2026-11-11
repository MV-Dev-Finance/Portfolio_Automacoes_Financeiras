import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from kit import render_all
from screens_a import SCREENS_A
from screens_b import SCREENS_B
from screens_c import SCREENS_C
out=os.path.join(os.path.dirname(__file__),'..','assets','screens')
if __name__=="__main__":
    only=sys.argv[1] if len(sys.argv)>1 else None
    allv={**SCREENS_A,**SCREENS_B,**SCREENS_C}
    if only: allv={k:v for k,v in allv.items() if only in k}
    render_all(allv,out); print(len(allv))
