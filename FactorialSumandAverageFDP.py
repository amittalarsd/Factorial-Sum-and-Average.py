#!/usr/bin/env python
# coding: utf-8

# In[3]:


def findFact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    fact = 1
    for i in range(1, n+1):
        fact = fact * i

    return fact
print(findFact(5))
print(findFact(-5))
print(findFact(0))


# In[4]:


def findSumAndAvg(aList):
    sum = 0
    avg = 0
    for n in aList:
        sum = sum + n
    
    avg = sum / len(aList)
    return [sum,avg]

print(findSumAndAvg([1,2,3,4,5]))
print(findSumAndAvg([0,-1,0,-1,0]))

