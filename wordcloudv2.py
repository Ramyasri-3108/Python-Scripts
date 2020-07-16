#!/usr/bin/env python
# coding: utf-8

# In[18]:


# make sure that all packages are successfully installed

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')   


# In[19]:


import fileupload
import io

def _upload( ):

    _upload_widget = fileupload.FileUploadWidget( )
       
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# In[20]:


def text_preprocess(file_contents):
    all_words=file_contents.split()
    #print(all_words)
    # Identify words containing punctuation
    p='''!@#$%^&*()_-':;/?\,.' '" "'''
    uninteresting_words=["a","an","the","to","for","if","and","will","in","of","at","be","on","by","with","as","just"," ","have","has","had","do","did","done","he","she","it","they"]
    temp_list=[]
    for w in all_words:
      word=""
      if (not w.isalpha()):  # if word do not contain all aplhabets
        for ch in w:
          if ch not in p:
            word=word+ch     # remove punctuation from word
        if (word not in uninteresting_words):
          temp_list.append(word)           # add punctuation removed word to list when the word is not in uninteresting words list
      else:
        if (w not in uninteresting_words): # if word is not in interesting words list
          temp_list.append(w)              # add word to list
    return (temp_list)

word_list=text_preprocess(file_contents)


# In[21]:


# Calculate frequencies of each word using dictionary

def calculate_frequencies(word_list):
  dic={}
  for word in word_list:  # for each word in list
    if(word not in dic):
      dic[word]=1         # add word as key
    dic[word]+=1          # increment count
  return dic

word_freq=calculate_frequencies(word_list)
#print(word_freq)


# In[22]:


# Generate word cloud 

import wordcloud
import matplotlib.pyplot as plt
cloud = wordcloud.WordCloud()
#cloud.to_file("mywordcloud.jpg")  # to generate wordcloud as a file 
myimg=cloud.generate_from_frequencies(word_freq)
plt.imshow(myimg, interpolation='nearest')
plt.axis("off")
plt.imshow(myimg)


# In[ ]:




