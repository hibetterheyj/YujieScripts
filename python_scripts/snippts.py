m# -*- coding: utf-8 -*-
"""
snippts
"""

## 从txt读取文件
# https://blog.csdn.net/shandong_chu/article/details/70173952
#read txt method three
f2 = open("./image/abc.txt","r")
lines = f2.readlines()
for line in lines:
    print line
    
## 取奇数偶数
numArr = [i for i in range(1,10)]
wArr = numArr[::2] # odd 奇数位置
hArr = numArr[1::2] # even 奇数位置

## 创建列表
r = [-1] * 5 # 创建空列表
r = [[]] * 5 # 创建-1列表
r = [-float('inf') for i in range(5)] # 循环方式不是特别优雅
"""
不推荐使用 r = [[0]*2] * 3
>>> r = [[0]*2] * 3
>>> r
[[0, 0], [0, 0], [0, 0]]
>>> r[0][1] = 3
>>> r
[[0, 3], [0, 3], [0, 3]] # not deepcopy !!!
"""

## 计算时间
#注：程序执行时间=cpu时间 + io时间 + 休眠或者等待时间
import time
start = time.clock() # time.time()
def naiveFib(n):
    if n==1 or n==0:
        return 1
    return naiveFib(n-1) + naiveFib(n-2) 
b = naiveFib(35)
end = time.clock() # time.time()
print(end-start)

## 多行处理的机制
# 修改自 https://blog.csdn.net/heshiip/article/details/86511406
lines=[]
while True:
    try:
        inputArray = input().split()
        numArray = [int(ele) for ele in inputArray]
        lines.append(numArray)
    except:
        break
    
## 单行读取转化为int列表
singleLine = input().split()
dim = [int(ele) for ele in singleLine]