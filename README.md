# AKDSFramework
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

### Contributing
Contributions are welcome. Make PR or open a new issue with some idea.