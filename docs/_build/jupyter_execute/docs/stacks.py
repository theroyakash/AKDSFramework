#!/usr/bin/env python
# coding: utf-8

# # Stacks
# 
# A stack is like an array but with limited functionality. You can only push to add a new element to the top of the stack, popto remove the element from the top, and peek at the top element without popping it off. Why would you want to do this? Well, in many algorithms you want to add objects to a temporary list at some point and then pull them off this list again at a later time. Often the order in which you add and remove these objects matters. A stack gives you a LIFO or last-in first-out order. The element you pushed last is the first one to come off with the next pop. (A very similar data structure, the queue, is FIFO or first-in first-out.)

# For example, let's push a number on the stack:
# 
# `stack.push(10)`
# The stack is now `[ 10 ]`. Push the next number:
# 
# `stack.push(3)`
# The stack is now `[ 10, 3 ]`. Push one more number:
# 
# `stack.push(57)`
# The stack is now `[ 10, 3, 57 ]`. Let's pop the top number off the stack:
# 
# `stack.pop()`
# This returns 57, because that was the most recent number we pushed. The stack is `[ 10, 3 ]` again.
# 
# `stack.pop()`
# This returns 3, and so on. If the stack is empty, popping returns nil or in some implementations it gives an error message ("stack underflow"). A stack is easy to create in python. It's just a wrapper around an array that just lets you push, pop, and look at the top element of the stack:
# AKDSFramework has a built in stack module. These are linked list and array based stacks and supports numerous operations.

# Let's first use the array based stack. To use array based stack import the following

# In[1]:


from AKDSFramework.structure.stack import ListBasedStack


# In[8]:


# Create a Stack based on array.
# Args:
#     - Array (list): Pass in an array to initialize the stack. If nothing is passed a blank stack is intialized.

stk = ListBasedStack()


# Now to push a few value into the stack we can use the stack push method, and also to pop a few element we can use pop method in stack. If `pop()` is called on a blank stack error will be generated.

# In[9]:


for i in range(2, 10):
    stk.push(i**2)


# In[10]:


print(stk)


# Now lets delete a few elements

# In[11]:


stk.pop()
print(f"After deletion stack is: {stk}")


# Here are a few supporting functions on the stack class.

# In[13]:


# Check the length of the stack. Length is stored in an internal variable so it's a O(1) time
print(len(stk))


# In[14]:


# Search for an element in the stack
print(f"Index of 16 is {stk.searchFor(16)}")


# In[15]:


# Remove all elements from the stack
stk.clear()


# As now we don't have element in the stack, running a pop() operation will generate an error

# In[16]:


stk.pop()


# Notice that a push puts the new element at the end of the array, not the beginning. Inserting at the beginning of an array is expensive, an O(n) operation, because it requires all existing array elements to be shifted in memory. Adding at the end is O(1); it always takes the same amount of time, regardless of the size of the array.
# 
# Fun fact about stacks: Each time you call a function or a method, the CPU places the return address on a stack. When the function ends, the CPU uses that return address to jump back to the caller. That's why if you call too many functions -- for example in a recursive function that never ends -- you get a so-called "stack overflow" as the CPU stack has run out of space.
