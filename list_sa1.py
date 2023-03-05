#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)


# In[2]:


#Exercise 2: Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20

print(tuple1[1][1])


# In[3]:


#Exercise 3: Create a tuple with single item 50
tuple1= (50, )
print(tuple1)


# In[4]:


#Exercise 4: Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)


# In[6]:


#Exercise 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)


# In[11]:


# ex 6 Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)


# In[15]:


#ex 7 Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# In[13]:


#Exercise 8: Sort a tuple of tuples by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)


# In[22]:


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1),key= lambda x: x[0], reverse=True))
print(tuple1)


# In[23]:


# Ex 9 Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))


# In[36]:


#Ex 10 Check if all items in the tuple are the same
def check(t):
    a=t[0]
    for i in t:
        if(i!=a):
            return False
    return True
tuple1 = (45, 45, 45, 45)
print(check(tuple1))


# In[37]:


def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))


# In[39]:


# ex 11 Check if an Item Exists in the Python Tuple
languages = ('Python', 'Swift', 'C++')

print('C' in languages)    # False
print('Python' in languages)    # True


# In[40]:


# ex 12 Write a Python program to compute the element-wise sum of given tuples.

x = (1,2,3,4)
y = (3,5,2,1)
z = (2,2,3,1)
print("Original lists:")
print(x)
print(y)
print(z)
print("\nElement-wise sum of the said tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)


# In[46]:


# Ex 13 Write a Python program to convert a tuple of string values to a tuple of integer values. 
def tuple_int_str(tuple_str):
    result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    return result
     
tuple_str =  (('333', '33'), ('1416', '55'))
print("Original tuple values:")
print(tuple_str)
print("\nNew tuple values:")
print(tuple_int_str(tuple_str))


# In[47]:


# Ex 14 Write a Python program to remove an empty tuple(s) from a list of tuples.

L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


# In[52]:


L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
s = []
for t in L:
    if t != ():
        s.append(t)
print(s)


# In[53]:


# ex 15 Write a Python program to convert a list of tuples into a dictionary.
#create a list
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)


# In[ ]:




