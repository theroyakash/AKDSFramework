<h1 align="center">
  <br>
  <a href="https://github.iamroyakash.com/AKDSFramework-docs"><img src="https://i.imgur.com/uDSHEhr.png" alt="AKDSFramework" width="800"></a>
  <br>
  <br>
</h1>

# AKDSFramework
[![AttentionNet Build Status](https://github.com/theroyakash/AKDSFramework/workflows/AKDSFramework/badge.svg)](https://github.com/theroyakash/AKDSFramework/actions)
[![Python3](https://img.shields.io/badge/python-3.8-blue.svg)](https://github.com/theroyakash/reddit-api)
[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/theroyakash/AKDSFramework/blob/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-theroyakash-red)](https://www.iamroyakash.com/contact)
[![GitHub license](https://img.shields.io/badge/Privacy-Policy-blue)](https://www.iamroyakash.com/privacy)

Python Package for all your data structure and algorithm needs.
AKDSFramework is a Purely written in Python library containing implementations 
of various data structures.

Our Package will allow user to focus on developing algorithms 
and not worry about finding python-compatible implementations of 
classic data structures like linked list, heap and others.

## Setup
- First download/clone this repo like git clone `https://github.com/theroyakash/AKDSFramework.git`
- Now uninstall if any previous version installed `pip3 uninstall AKDSFramework`
- Now install fresh on your machine `pip3 install -e AKDSFramework`

### Alternate installation
This is easier to install but a bit slower in the installation time.
`pip3 install https://github.com/theroyakash/AKDPRFramework/tarball/main`

## First code, Check the version
Now to check whether your installation is completed without error import AKDSFramework
```python
import AKDSFramework
print('AKDSFramework Version is --> ' + AKDSFramework.__version__)
```
## Example code creating Linked List
```python
from AKDSFramework.structure.linkedlist import SinglyLinkedList

lkl = SinglyLinkedList()
# Now add some data into it
lkl.add(20)
lkl.add(120)
lkl.add(7102)
lkl.add(773)

# Now to see your linked list
print(lkl)   # ---> 20 --> 120 --> 7102 --> 773 --> None
# Now reverse this linked list:
print(reversed(lkl))
```

## Supported python APIs
### LinkedList
AKDSFramework currently supports the singly linked list data structure, in future we’ll add the circular and the doubly linked lists. When the installation done to use linked list just import the following code

```python
from AKDSFramework.structure import SinglyLinkedList
singlelinkedlist = SinglyLinkedList()
```

```python
# Now add a few nodes to the list
singlelinkedlist.add(2)
singlelinkedlist.add(49)
singlelinkedlist.add(82)
singlelinkedlist.add(21)
```
Now we need to be able to see how the linked list currently looks like. So to do that simply call `print()` method.
```
print(singlelinkedlist)
```
This will return `2 --> 49 --> 82 --> 21 --> None`
Now we have our linked list. Now we can do some operations on it. We currently support the following operations on linked lists.

| ID | Operation call method                 | What does it do?                                    |
|----|---------------------------------------|-----------------------------------------------------|
| 1  | `.add()`                              | Add value at the very end.                          |
| 2  | `for _ in singlelinkedlist:`          | Iterates over the linked list                       |
| 3  | `.removeAt(index)`                    | Mention the index you want the value to be removed. |
| 4  | `.get_head()`                         | Get the head node value of the linked list          |
| 5  | `.count()` or `len(singlelinkedlist)` | Total number of element in the list                 |
| 6  | `.isEmpty()`                          | Returns True if list is empty                       |
| 7  | `reversed(singlelinkedlist)`          | Reverses the linked list                            |
| 8  | `singlelinkedlist[index]`             | Get the data at index = index                       |
| 9  | `.prettyprint()`                      | Not implemented yet                                 |
| 10 | `print(singlelinkedlist)`             | Prints the linked list in a nice format.            |


### Heap
Building heap was never been this easy. Follow these steps
- First make a heap by importing Heap from AKDSFramework.
```python
from AKDSFramework.structure import MaxHeap, MinHeap
```
- Now let's build a max heap with 15 values.
```python
mxheap = MaxHeap([data**2 for data in range(15)])
```
- Now it's important to call the build method on the heap to build the heap from an unstructed array of numbers. If the build is not done printing and doing operations on heap will not be valid and will generate HeapNotBuildError. So always build your heap with `.heap()` method if you caused any change in the heap structure. Each time calling `.build()` method will use `O(logN)` time.
```python
mxheap.build()

# Now add few elements to the heap
mxheap.add(12)
mxheap.add(4)

# As the heap structure is changed so we have to call .build() again
mxheap.build()
```
- Now lets print the heap:
```py
print(mxheap)
```
This will return `[2744, 1331, 2197, 729, 1000, 1728, 343, 512, 64, 8, 125, 1, 216, 27, 12, 4]` and you also have the ability to see the heap printed prettyly by using prettyprint() method.

```py
mxheap.prettyprint()
```

### Sorting
AKDSFramework supports multiple sorting techniques. Among them bubble sort, insertion sort and heapsort is available currently.

For bubble sort and insertion sort we maintain a dictionary of internal array positions for future use, If you don't want to store each internal state of array simply mention `maintain_iter_dict` = `False`

You can also visualize without maintaining a dictionary by using flag `vizualize` = `True`. Both are set `False` by default.

Below is an example of using the internal state dictionary animating each step of bubble sort.
```python
from AKDSFramework.applications.sorting import bubblesort, insertionsort, heapsort

# For visualization and sorting
from matplotlib import pyplot as plt
import matplotlib.animation as animation

a = [x + 1 for x in range(50)]
random.seed(time.time())
random.shuffle(a)

a, iter_dict = bubblesort(a, False, True)

def get_array_generator(iter_dict):
    for key in iter_dict:
        yield iter_dict[key]

generator = get_array_generator(iter_dict)

fig, ax = plt.subplots()
ax.set_title("Bubble Sort animation")
bar_rects = ax.bar(range(len(a)), a, align="edge")

# Set axis limits. Set y axis upper limit high enough that the tops of the bars won't overlap with the text label.
N = len(a)
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.5 * max(a)))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]

def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, iteration), frames=generator, interval=1,
    repeat=False)
plt.show()
```

### Contributing
[![GitHub license](https://img.shields.io/badge/CONTRIBUTING-Welcome-blue)](https://github.com/theroyakash/AKDSFramework/pulls)

Contributions are welcome. Make PR or open a new issue with some idea.