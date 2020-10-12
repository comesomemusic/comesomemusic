import re
from fractions import Fraction
def do_math(s):
    S1=re.sub(r"'",'+',s)
    S2=re.sub(r'(\d+/\d+)',r'(\1)',S1)
    S3=re.sub(r"=",'',S2)
    S4=re.sub(r'(\d+)', r'Fraction("\1")',S3)
    
    try:
        answ=eval(S4)
        return answ
    except Exception as e:
        print(e)
        return -1

a=[]
a.append('(1 - (4/5) + 4) =')
a.append("(6 + (2'(4/7)) / 3) = ")
a.append("(1/3) * (2/3) * ((6'(2/7)) * 4 - (1/4)) =")
a.append('(4 / ((2 - 0) + (3/6))) = ')
a.append('(4 / (4/5) + (1/2)) = ')
a.append("((9/10) * ((3'(9/10)) * (2'(1/3))) / (3/5)) + (6/7) = ")
a.append("(1 / ((3/4) / (2'(1/4)) * 2)) =" )
a.append("((4'(2/3)) * 2 * (1'(1/4))) - (4'(4/5)) = ")
a.append("((6'(1/5)) + (4'(1/5)) * (3/4)) = ")
a.append('(1 + 1 / 2) = ')
for i in range(1,11):
    print(a[i]+str(do_math(a[i])))

