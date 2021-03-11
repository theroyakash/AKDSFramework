#!/usr/bin/env python
# coding: utf-8

# # Queue
# A queue is a list where you can only insert new items at the back and remove items from the front. This ensures that the first item you enqueue is also the first item you dequeue. First come, first serve! Why would you need this? Well, in many algorithms you want to add objects to a temporary list and pull them off this list later. Often the order in which you add and remove these objects matters. A queue gives you a FIFO or first-in, first-out order. The element you inserted first is the first one to come out. It is only fair! (A similar data structure, the stack, is LIFO or last-in first-out.)

# A queue is not always the best choice. If the order in which the items are added and removed from the list is not important, you can use a stack instead of a queue. Stacks are simpler and faster.
# 
# To make a queue import the followings

# In[1]:


from AKDSFramework.structure import ArrayQueue


# Now let's create a queue. You need to pass an capacity argument to initialize a static array in memory. `capacity (int)`: Creates a None value static array with specified capacity.

# In[2]:


q = ArrayQueue(4)


# In[3]:


q.enqueue(12)
print(q)


# In[4]:


# Now let's add a few queue members
q.enqueue(2)
q.enqueue(112)
q.enqueue(645)


# In[5]:


print(q)


# You can also dequeue elements from the begining of the list

# In[6]:


dequeuedelement = q.dequeue()


# In[8]:


print(dequeuedelement)
print(q)


# In[9]:


dequeuedelement2 = q.dequeue()
print(dequeuedelement2)
print(q)


# ## See also
# There are many ways to create a queue. Alternative implementations use a linked list, a circular buffer, or a heap. Variations on this theme are deque, a double-ended queue where you can enqueue and dequeue at both ends, and priority queue, a sorted queue where the "most important" item is always at the front.
