#!/usr/bin/env python
# coding: utf-8

# # Benchmarking and caching decorators
# Let's say you have a really slow program and you want to benchmark where your program is taking most of the time to run. If you can find that you can just optimize that part of the program to run faster.
# 
# There is couple of way of doing this going through this manually or using some kind of library like cProfile to generate a report on the function's workings.
# 
# You can pretty much use this on any python function as you like, small-big-has other dependency anything.
# 
# Let's see a few example as how to use these Benchmarking decorator.

# In[1]:


from AKDSFramework.applications.decorators import benchmark


# Now after importing we write a function and before the function we mention @benchmark and it'll generate reports of the innerworkings of the function.
# 
# We gonna see an example of implementation of benchmarking by building a max heap and adding 2 numbers to the heap and again building it. To make max heaps I'll use AKDSFramework, let's create a heap and build it now with around 600 elements.

# In[2]:


from AKDSFramework.applications.decorators import benchmark
from AKDSFramework.structure import MaxHeap

@benchmark
def buildHeap(array):
    h = MaxHeap(array)
    h.build()

    h.add(68)
    h.add(13)
    h.build()

buildHeap([data**2 for data in range(601)])


# Notice the @benchmark decorator at the beginning of the declaration of the function, that calls cProfile to start calculating what taking what.
# 
# This has all the call's report and how much time it's taking. If you see the second last function call `{method 'append' of 'list' objects}` see that's called 2 times total as we are appending 2 elements.
# 
# So this way you can see how much each function taking time and how many times they are called. If you wish you can reduce the number of calls or use a different approach to solve the part where it's slow.

# ## Caching
# Now there is now way you can optimize the function, what you can do instead is that you can store results from a previous computation and reuse those results in a new computation to find solutions to other problem.
# 
# Let's create world's worst fibonacci series computation code. The algorithm might look like this:
# 
# ```
# FIBONACCI (n):
#     if n -> 0: f = 0
#     elif n -> 1: f = 1
#     else:
#         f = FIBONACCI(n - 1) + FIBONACCI (n - 2)
#     return f
# ```

# This is a correct algorithm for fibonacci. But if you see the recurrence relation T(n) = T(n-1) + T(n-2) + O(1) you can see that the code is running in exponential time O(2^N) which is really really bad.
# 
# The equivalent python code would be:

# In[3]:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# If you draw a recursion tree you can find that you are computing same computation over and over again in different trees. Let's see what I mean:
# 
# ```
# +--+-----------+-----------+--------+-----------+-----------+--+
# |  |           |           | Fib(n) |           |           |  |
# +--+-----------+-----------+--------+-----------+-----------+--+
# |  |           | Fib (n-1) |        | Fib (n-2) |           |  |
# +--+-----------+-----------+--------+-----------+-----------+--+
# |  | Fib (n-2) | Fib (n-3) |        | Fib (n-3) | Fib (n-4) |  |
# +--+-----------+-----------+--------+-----------+-----------+--+
# ```

# See for calculating fib(n) you are calculating Fib (n-1) and Fib (n-2). In a separate computation you are computing Fib (n-2) for that you are computing Fib (n-3) and Fib (n-4).
# 
# If you had Fib (n-2) from the previous computation stored, you wouldn't have to recompute that Fib (n-2) and it's subsequent branches. So you would've saved a lot of time by just not recomputing anything.
# 
# Let's without caching how much time it would take to compute fib(35) that is 35th fibonacci number:

# In[5]:


import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.perf_counter()
print(fibonacci(35))
end = time.perf_counter()

print(f"Computed in {(end - start)} seconds")


# Total time for computation is 4.039259026000025 seconds. So our python program is taking 4.039259026000025 seconds to compute fib(35). Now let's store intermediate step's data in a dictionary so that we can retrieve those data at a later time in constant time.
# 
# First we import the caching decorator.

# In[6]:


from AKDSFramework.applications.decorators import cached


# Now we write the function but with the caching decorator.

# In[7]:


import time

@cached
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


start = time.perf_counter()
print(fibonacci(40))
end = time.perf_counter()

print(f"Computed in {(end - start)} seconds")


# Now it takes around 0.0004765559999668767 seconds, which is a huge heap in performance.
