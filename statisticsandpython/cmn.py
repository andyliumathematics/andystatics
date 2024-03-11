# %%
from scipy.special import perm, comb
# 排列
perm(5,4)
# %%
# 组合
comb(5,4)
# %% 列出所有可能
from itertools import combinations
combins = [c for c in  combinations(range(5), 2)]
print(combins)
# %% 列出所有可能
from itertools import permutations
perms =  [c for c in   permutations(range(5), 2)]
print(perms)
# %%
range(5)
# %%
# 条件概率
S = set({1,2,3,4,5,6})
A1 = set({1,2,3})
# %%
A1&S

# %%
S-A1
# %%
A2=set([1, 2, 3]) 
# %%
A2
# %%
print('S=%s:抛掷骰子的样本空间.'%S)

# %%
print('A1=%s:偶数点.'%A1)
# %%
print('A2=%s:点数不超过3.'%A2)
# %%
print('A1+A2=%s:偶数点或点数不超过3.'%(A1|A2))   	#A1∪A2：偶数点或点数不超过3
# %%
print('A1*A2=%s:不超过3的偶数点.'%(A1&A2))       	#A1∩A2：不超过3的偶数点

# %%
print('A1-A2=%s:超过3的偶数点.'%(A1-A2))         	#超过3的偶数点

# %%
print('Ā1=%s:奇数点.'%(S-A1))                    #A1的补集（A1的对立事件）
# %%
print('(A1+A2)_=Ā1*Ā2 is %s.'%(S-(A1|A2)==(S-A1)&(S-A2)))
# %%
print('(A1*A2)_=Ā1+Ā2 is %s.'%(S-(A1&A2)==(S-A1)|(S-A2)))
# %%
