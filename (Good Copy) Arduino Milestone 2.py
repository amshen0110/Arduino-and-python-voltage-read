#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pyfirmata as pf
from jupyterplot import ProgressPlot
import time


# In[2]:


board = pf.Arduino("COM4")
it = pf.util.Iterator(board)
it.start()


# In[3]:


a0 = board.get_pin('a:0:i')


# In[4]:


a0.read()


# In[5]:


pp = ProgressPlot(x_label="Voltage in Volts (y) vs Time (x) Graph", x_lim=[0, 1000], y_lim=[0, 5], line_names = ["Voltage"]) #Adding syntax to graph
for i in range(1000):
    z= a0.read()*5 #in order to output to scale voltage values on graph
    pp.update(z)
    time.sleep(0.1) #creating a time delay of 0.1 seconds
pp.finalize()

