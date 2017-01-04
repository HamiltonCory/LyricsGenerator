
# coding: utf-8

# In[3]:

from gensim import corpora, models


# In[4]:

#dictionary=corpora.Dictionary(texts)


# In[65]:

#location='C:\Users\Cory\Downloads\TestDataset-20170104T000550Z\TestDataset'
location='C:\Users\Cory\Downloads\Songs'
print(location)


# In[66]:

import os
indir = location
nested_content=[]
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        with open("{0}/{2}".format(location, dirs, f)) as fname:
            nested_content.append(fname.readlines())
            #print(content)


# In[67]:

nested_content[0]


# In[68]:

dictionary=corpora.Dictionary(nested_content)
#print(dictionary)
print(dictionary[0])


# In[69]:

corpus=[dictionary.doc2bow(text) for text in nested_content]


# In[70]:

corpus


# In[ ]:



