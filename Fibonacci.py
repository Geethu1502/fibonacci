#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("number of terms"))
n1=0
n2=1
count=0
if n<=0:
    print("enter the positive numbers")
elif n==1:
    print("Fibonacci upto",n,":")
    print(n1)
else:
    print("Fibonacci :")
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1


# In[ ]:




