# %%
"""按条件设置随机事件
https://blog.csdn.net/u012958850/article/details/116330514?spm=1001.2014.3001.5501
"""


# %%
def subSet(S, condition):
    A = set()
    for x in S:
        if condition(x):
            A.add(x)

    return A


# %%
from sympy.utilities.iterables import variations as permutations

S = set(permutations([0, 1], 3, True))  # 样本空间
A1 = subSet(S, lambda x: x[0] == 1)  # 事件A1 第一枪命中
A2 = subSet(S, lambda x: x[1] == 1)  # 事件A2 第二枪命中
A3 = subSet(S, lambda x: x[2] == 1)  # 事件A3  第三枪命中
A_1 = S - A1  # 第一枪未命中的情况
A_2 = S - A2
A_3 = S - A3

print(A1|A2|A3)           #至少命中一枪
print(A1&A2&A3 )        # 三枪都击中
print(A1-A2-A3)
# %%
A_1
# %%
S
# %%
A1
# %%
