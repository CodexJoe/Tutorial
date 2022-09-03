#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''This fnction calculates the floor division of the 
following mathematical expression ((x+12)^2-y^3)) by 9'''



def My_F():#This create a function names My_F
    X=input('Please Enter Value For X: ') #This gets value for X from the Outside
    X=int(X) #This Cast the obtained value for X into datatype integer
    Y=input('Please Enter Value For Y: ') #This gets value for Y from the Outside
    Y=int(Y) #This Cast the obtained value for Y into datatype integer
    Z=((X+12)**2-(Y**3))//9 #This performs the giving operation and  stores the result into variable Z
    return(Z) #This stores the value of Z in the program memory for future use


print(My_F()) #This calls out the functiona and prints it on the screen.

