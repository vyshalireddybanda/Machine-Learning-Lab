#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sqlite3


# In[11]:


conn = sqlite3.connect('exp2.db')
cur = conn.cursor()
#conn = sqlite3.connect('test.db')
print("Opened database successfully!");


# In[20]:


conn.execute('''CREATE TABLE COMPANY3
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        AGE  INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL);''')
print("Table created successfully!");


# In[21]:


conn.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY3 (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print ("Records created successfully");


# In[22]:


for row in conn.execute('select * from COMPANY3'):
        print(row)


# In[23]:


conn.commit()


# In[24]:


conn.close()


# In[ ]:




