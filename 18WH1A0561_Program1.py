#!/usr/bin/env python
# coding: utf-8

# In[4]:


probabilityAbsentAndFriday = 0.03
probabilityFriday = 0.2
print("Probability that it is Friday and the student is absent : ",probabiltyAbsentAndFriday)
print("Probabilty that it is Friday : ",probabilityFriday)
#on applying bayes theorem
bayesResult = (probabiltyAbsentAndFriday/probabiltyFriday)
print("Probability that a student is absent given that today is Friday : ",bayesResult*100)


# In[ ]:




