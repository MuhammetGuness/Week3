#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
array = np.array([0, 1, 2, 3, 4, 5, 6, 7])
array1 = np.zeros((2,5))
array2 = np.ones([5])
array3 = np.array([[1,2,3],[4,5,6]])
print(array)
print(array1)
print(array2)
print(array3)


# In[41]:


#Belirlenen boyutlarda birim matris oluşturmamızı sağlayan fonksiyon.
array4 = np.eye(3,5)
print(array4)
print("///////////")
array45 = np.eye(5)
print(array45)


# In[42]:


#rastgele dizi oluşturmak için kullanılır. random.randomdan farklı olarak iki parametre (satır,sutun vb.gibi) alır
array5 = np.random.randn(3,5)
array6 = np.random.rand(10)
print(array5)
print("///////////")
print(array6)
print("///////////")
array7 = np.random.rand(3,5)
array8 = np.random.rand(10)
print(array7) 
print("///////////")
print(array8)


# In[55]:


array9 = np.matrix([[5,5],[4,7]])*2
print(array9)
array9 = np.matrix('1 2; 3 4')
print(array9)


# In[ ]:




