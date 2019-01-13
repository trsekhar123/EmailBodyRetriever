
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='EmailBodyRetriever',
    version='0.1dev',
    packages=['email_body_retriever',],
    author='Rajasekhar Thiruthuvaraj',
    author_email='trsekhar.123@gmail.com',
    url='https://github.com/trsekhar123/EmailBodyRetriever',
    license='MIT',
    long_description=open('README.md').read(),
)

