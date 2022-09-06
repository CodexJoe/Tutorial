#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Question 1: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

Sample value of n is 5 

Expected Result : 615 (5+55+555)'''




a = (input("Input an integer : "))
n1 =  (a)
n2 = a+a
n3 = a+a+a
print(n2)
print(n3)

Result = int(n1) + int(n2) + int(n3)
print(Result, 'is the result of n+nn+nnn')


# In[ ]:




