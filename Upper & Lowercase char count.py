#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#HINT: Two string methods that might prove useful: .isupper() and .islower()

def up_low(s):
    uppercase = 0
    lowercase = 0
    
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
        
    print(f'Original String: {s}')
    print(f'No. of upper case characters: {uppercase}')
    print(f'No. of lower case characters: {lowercase}')


# In[3]:


s = 'Hi there people! My name is Sanath Kapoor!'
up_low(s)


# In[ ]:




