#!/usr/bin/env python
# coding: utf-8

# In[2]:


i = 5
if i<5:
    print("Küçüktür")
elif(i==5):
    print("Eşittir")
else:
    print("Büyüktür")


# In[ ]:


sum = 0
for num in range(1,10):
    sum += num
print(sum)


# In[9]:


total = 0
x = 10
while x>5:
    total += x
    x -= 1
print(total)


# In[14]:


def printfunc(a):
    print("Sayı : " , a)
    
printfunc(8)


# In[ ]:




