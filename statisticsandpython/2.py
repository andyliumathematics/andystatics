# %%
'''
排列组合——构造样本空间
https://blog.csdn.net/u012958850/article/details/116330470?spm=1001.2014.3001.5501`
'''
from sympy.utilities.iterables import variations,subsets
# 最后一个参数True表示数组中的数据结果中可重复，如果是Fals，则结果中不可重复
# 这个重复不重复，更像是随机试验里是否放回。
# 排列
S1 = set(variations([1,2],3,True))
# 组合
S2= set(subsets([1,2],3,True))
print(S1)
print(S2)
# %%
# 10个人中选择三个人
print(len(set(variations(range(1,11),3,False))))
# %%
