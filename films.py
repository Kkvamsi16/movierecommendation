#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
movies=pd.read_csv('dataset1.csv')


# In[49]:


movies.head(10)


# In[50]:


movies.describe()


# In[51]:


movies.info()


# In[52]:


movies.isnull().sum()


# In[53]:


movies.columns


# In[54]:


movies=movies[['id','original_title','overview','genres']]


# In[55]:


movies


# In[56]:


movies = movies.assign(tags=movies['overview'] + movies['genres'])


# In[57]:


movies.loc[:, 'tags'] = movies['overview'] + movies['genres']


# In[58]:


movies


# In[59]:


new_data=movies.drop(columns=['overview','genres'])


# In[60]:


new_data


# In[61]:


from sklearn.feature_extraction.text import CountVectorizer


# In[62]:


cv=CountVectorizer(max_features=10000,stop_words='english')


# In[63]:


cv


# In[64]:


vector=cv.fit_transform(new_data['tags'].values.astype('U')).toarray()


# In[65]:


vector.shape


# In[66]:


from sklearn.metrics.pairwise import cosine_similarity


# In[67]:


similarity=cosine_similarity(vector)


# In[68]:


similarity


# In[69]:


new_data[new_data['original_title']=="Furious 7"].index[0]


# In[70]:


distance=sorted(list(enumerate(similarity[2])),reverse=True,key=lambda vector:vector[1])
for i in distance[0:5]:
    print(new_data.iloc[i[0]].original_title)


# In[71]:


def recommand(movies):
    index=new_data[new_data['original_title']==movies].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector:vector[1])
    for i in distance[0:5]:
        print(new_data.iloc[i[0]].original_title)
    


# In[72]:


recommand("Minions")


# In[73]:


import pickle


# In[74]:


pickle.dump(new_data,open('movies_list.pkl','wb'))


# In[75]:


pickle.dump(similarity,open('similarity.pkl','wb'))


# In[76]:


pickle.load(open('movies_list.pkl','rb'))


# In[ ]:





# In[ ]:




