#!/usr/bin/env python
# coding: utf-8

# In[10]:


FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"


# In[11]:


swimmer, age, distance, stroke = FN.removesuffix('.txt').split('-')


# In[12]:


with open(FOLDER+FN) as df:
    data = df.readlines()
times = data[0].strip().split(',')


# In[13]:


converts = []
for t in times:
	minutes,rest = t.split(':')
	seconds,hundredths = rest.split('.')
	converts.append(int(minutes)*60*100 + int(seconds)*100 + int(hundredths))


# In[14]:


import statistics
avg = statistics.mean(converts)
mins_secs, hundredths = str(round(avg/100,2)).split(".")
mins_secs = int(mins_secs)
minutes = mins_secs//60
seconds = mins_secs-minutes*60
average = str(minutes) + ":" + str(seconds) + "." + hundredths


# In[15]:


swimmer, age, distance, stroke


# In[16]:


times


# In[17]:


average


# In[ ]:




