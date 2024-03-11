# %%
from sympy import Rational
from sympy.utilities.iterables import variations
Rational(3,4)
# %%
S = set(variations([0,1],3,True))
# %%
def oneCondition(s,condition):
    A=set()
    for i in s:
        if condition(i):
            A.add(i)
    return A

# %%
A3 = oneCondition(S, lambda x: x[0]==1 & x[1]==1 & x[2]==1)  # 事件A3  第三枪命中

# %%
A3

# %%
Rational(len(A3),len(S))

# %%
# 房内10个人例题
from sympy.utilities.iterables import subsets as combinations

# %%
numbers =range(1,11)
# %%
set(numbers)
# %%
S  = set(combinations(set(numbers),3))

# %%
def P(A,S):
    n = len(S)
    m = len(A)
    return Rational(m,n)

# %%
A = oneCondition(S,lambda a:min(a)==5)
# %%
A
# %%
P(A,S)

# %%

B = oneCondition(S,lambda a:max(a)==5)
# %%
P(B,S)
# %%
