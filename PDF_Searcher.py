#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Data-Name-Extraction-Program
# import packages
import os

# define target directory
target = 'C:\\Users\\hille\\Desktop\\Masterarbeit\\Paper Lehrstuhl'

# performe extraction
content  = os.listdir(target)
directory = []
data = []
for elem in content:
    elem_path = os.path.join(target, elem)
    if os.path.isfile(elem_path):
        data.append(elem)
    if os.path.isdir(elem_path):
        directory.append(elem_path)
for basedirectory, directory, data in os.walk(target):
    break

    
    
print(basedirectory)
print(directory)
print(data)


# In[3]:


# Search-Program

# import packages
import PyPDF2
import re

# define keyterms
keys = ['WTI', 'Brent', 'maize', 'rice', 'soy', 'wheat', 'cocoa', 'coffee', 'cotton', 'sugar', 'cattle', 'corn'       , 'hogs']

# checked_kes = ['BIC', 'Akaike information criterion', 'Final Prediction Error criterion', 'FPE', 'Hannan-Quinn criterion'\
#        , 'HQ', 'Schwarz information criterion', 'SIC', 'Granger', 'likelihood ratio']
objects = data


for i in keys:
    key = i
    print('Search item: ' + str(key))

    # open the pdf file
    for i in objects:
        print('PDF: ' + str(i))
        object = PyPDF2.PdfFileReader(target + '\\' + i)
        # get number of pages
        NumPages = object.getNumPages()
            # define counter
        count = 0
        # extract text and do the search
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            #print("this is page " + str(i)) 
            Text = PageObj.extractText() 
                #print(Text)
            ResSearch = re.search(key, Text)
            if ResSearch == None:
                count = count
            else:
                count+=1
            #print(ResSearch)
        print(count)
    
print('Search completed')


# In[2]:


# Search-Program-Class

# import packages
import PyPDF2
import re

import pandas as pd
import numpy as np


# define keyterms
keys = ['BIC', 'Akaike information criterion', 'Prediction Error criterion', 'FPE', 'Hannan-Quinn criterion'        , 'HQ', 'Schwarz information criterion', 'SIC', 'Granger']
objects = data

def searcher(key, name, target):
    print('Search item: ' + str(key))
    
    print('PDF: ' + str(name))
    object = PyPDF2.PdfFileReader(target + '\\' + name)
    # get number of pages
    NumPages = object.getNumPages()
    # define counter
    count = 0
    # extract text and do the search
    for i in range(0, NumPages):
        PageObj = object.getPage(i)
        #print("this is page " + str(i)) 
        Text = PageObj.extractText() 
        #print(Text)
        ResSearch = re.search(key, Text)
        if ResSearch == None:
            count = count
        else:
            count+=1
                #print(ResSearch)
    print(count)
    return count


# In[12]:


import pandas as pd
import numpy as np

df = pd.DataFrame(columns=objects)
print(df)

for i in objects:
    df.i = 
for i in keys:
    key = i
    df[key].apply(searcher(key, objects))
    
    
    
def list_col(df, column, index, target):
    return (df[column]

print (list_col(df, 'F'))
['a', 'b', 'c']    
    
    
    
for index, row in df.iterrows():
    date = index
    Period = row.loc[row.index[0]]  
    LocationList = row.index[1:]
    print(date, Period)
    for Location in LocationList :
        PeriodDF.loc[(PeriodDF.index == date)&(PeriodDF.Period == Period), Location] = Get_Y(date, Period, Location)


# In[ ]:



for i in keys:
    key = i
    for i in objects: 
        name = i
               
        df.apply(searcher(key, name, target), axis=1, args=('col1', 'col2', 'col3'))
        
        
        
        
        searcher(key, name, target)


print('Search completed')




pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)],ignore_index=True)

    
    print(df)


# In[ ]:


def max_word_length(row, *cols):
    return row[list(cols)].map(len).max()

# Make sure `axis=1` so rows are passed in and we can access columns
df.apply(max_word_length, axis=1, args=('col1', 'col2', 'col3'))

