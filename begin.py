#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="Hello World"
print(len(a))


# In[2]:


txt="hellow the is the my area"
print("free" in txt)


# In[3]:


b="hello world"
print(b[2:7])


# In[4]:


b="hello world"
print(b[:5])


# In[5]:


b="hello world"
print(b[:-5])
print(b[-1])


# In[6]:


b="hello world"
print(b.strip())


# In[9]:


b="hello world"
print(b.upper())


# In[12]:


a="hello world"
print(a.replace("h" , "J"))


# In[16]:


a="hello world"
print(a.split("r"))


# In[19]:


a="hello"
b="hai"
c=a+" " +b
print(c)


# # not possible in python

# In[20]:


age = 36
txt = "My name is John, I am " + age
print(txt)


# # but we can do with format method

# In[22]:


old=40
a="my name disco,i am {}"
print(a.format(old))


# In[ ]:




