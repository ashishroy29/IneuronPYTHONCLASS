#!/usr/bin/env python
# coding: utf-8

# # Module

# In[1]:


import os


# In[2]:


#For Example:
#os is a module and based on thaat you will be able to work
#someone has already created tht for you and based on that you will be able to work
#how we will be able to create such kind of a file?
#In Modular coding we need to increase the reusability of the code
#its not like we need to write the code again and again


# In[3]:


# Understanding how to use modular coding


# In[4]:


# Modules are nothing but a set of a code or collection of a code which i can keep inside any of these files
#suppose we have created many functions
#i would like to reuse those functions again and again
# Trying to use logging each and everytime.
# We will just create once and use many times


# In[5]:


# Add function
def test(a,b):
    return a+b


# In[6]:


# we cannot identify the function if it is in one page and we are trying to find it on another page.
# I want to use same function in another jupyter notebook which is being opened and i dont want to rewrite that function again so this is my problem statement


# In[7]:


# Modules and packages
type()
print()
len()


# In[ ]:


pwd()


# In[ ]:


get_ipython().run_line_magic('ls', '')


# In[ ]:


# Before we start coding, make sure to download notepad++ and save .py file in the pwd()


# In[ ]:


get_ipython().run_line_magic('ls', '')


# In[8]:


import test1


# In[9]:


#test1 is a module name which we are trying to import will be available in jupyter notebook
#Suppose we are trying to import it in another notebook file we can import there aswell
#Make sure when you are doing it, the file should be in the current directory


# In[10]:


#reusinng the file
test1.test(3,4)


# In[12]:


test1.test4()


# In[13]:


#if it is not able to find the function then go for kernel restart because jupyter is not a good notebook, it will give you pain


# In[14]:


test1.test3(2,3)


# In[15]:


#Here we are trying to import only one method
from test1 import test3


# In[16]:


test3(2,3)


# In[17]:


#Here we are trying to import only one method
from test1 import test4


# In[18]:


test4()


# In[1]:


# here we are importing everything
from test1 import *


# In[21]:


test4()


# In[22]:


test3(1,2)


# In[23]:


test(1,3)


# In[24]:


l = [2,3,4,5,6]


# In[25]:


#l.presstab


# In[2]:


test(2,3)


# In[3]:


#https://docs.python.org/3/py-modindex.html


# In[4]:


#https://github.com/python/cpython/tree/3.10/Lib
#Checkout how to write a standaard grade code


# In[ ]:


len()


# In[6]:


dir()


# In[7]:


open("my_module.py","w")


# In[8]:


get_ipython().run_line_magic('ls', '')


# In[9]:


#Here we have created a custom module where we can add our own funnctions and call it in the libraries when required.
import my_module


# In[10]:


my_module.get_course()


# In[11]:


my_module.greetings()


# In[12]:


#in a project we will be able to finnd out many files, and also find out many directory structure


# In[13]:


#modules are nothing but one single file which we have created and written n number of funnctions


# In[3]:


#what are packages?
#Its about creating mulitiple files and packages thats it.
#packages are nothinng but collection of a modules, if we are wrinting multiple modules, and what are modules, it is nothing but .py file/ which includes n number of fucntions or classes
# It is nothing but a combinnation of folders and files
# Python files which we will keep under a single directory, it is called as packages, Theere is a possibility where we may create multiple packages,i will be able to create multiple modules inside packages


# In[4]:


#Creating new modlules and packages in python
#Directories are nothing but folders


# In[ ]:


# collection of modules are called as packages


# In[5]:


#ADVANTAGES OF USING PYCHARM
# it will give you auto pop up
# Auto completion is very easy


# In[6]:


#you can call a module in another python file and then use it accordingly.


# # ASSIGNMENT

# In[8]:


#Create a kind off of a tool by which you will be able to browse each and every file which is availabe inside a respective directory
#Annd it is supposed to show the files inn the tool


# In[9]:


#Task 2 : after this, same window, after listing all number of files, just in current directory if we have pdf file or not


# In[10]:


# If we have 0 pdf do nothing, if we have more than 1 pdf, merge all pdf and create a new pdf just on a click, We are looking for a final pdf in the saame current directory


# In[11]:


# we are supposed to create GUI Kiwi library


# In[12]:


#use libraries such as kivy, Tynkerkt, Tinker, wee can create this kind of a window.


# In[13]:


#Restrictions when using a code.
#1) Use logging
#2) Modular coding (Packaages annd modules we are supposed to create)

