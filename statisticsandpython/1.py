# %%
'''
随机事件的Python表示
https://blog.csdn.net/u012958850/article/details/116301279?spm=1001.2014.3001.5501
'''

# 骰子
S = set({1,2,3,4,5,6})
A1 = set({2,4,6})
A2 = set({1,2,3})
print('S=%s:抛掷骰子的样本空间.'%S)
print('S=%s:投掷骰子的偶数点'%A1)
print('S=%s:不超过3的点'%A2)
print('S=%s:偶数点且不超过3的点'%(A1&A2))
print('S=%s:偶数点或者不超过3的点'%(A1|A2))
print('S=%s:超过3的偶数点'%(A1-A2))
print('S=%s:奇数点'%(S-A1))
# print(A1*A2)
print('(A1+A2)_=Ā1*Ā2 is %s.'%(S-(A1|A2)==(S-A1)&(S-A2)))
print('(A1*A2)_=Ā1+Ā2 is %s.'%(S-(A1&A2)==(S-A1)|(S-A2)))
# %%
