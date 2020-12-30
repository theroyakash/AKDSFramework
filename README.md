<h1 align="center">
  <br>
  <a href="https://github.iamroyakash.com/AKDSFramework-docs"><img src="https://i.imgur.com/uDSHEhr.png" alt="AKDSFramework" width="800"></a>
  <br>
  AKDSFramework
  <br>
</h1>

<h4 align="center">Python Package for all your data structure and algorithm needs.</h4>

<p align="center">
  <a href="https://github.iamroyakash.com/AKDSFramework-docs/">Getting started</a> •
  <a href="https://github.iamroyakash.com/AKDSFramework-docs/docs/ds.html">Data Structures</a> •
  <a href="https://github.iamroyakash.com/AKDSFramework-docs/docs/searching.html">Algorithms</a> •
  <a href="https://github.com/theroyakash/AKDSFramework/blob/main/LICENSE">License</a>
</p>

[![AttentionNet Build Status](https://github.com/theroyakash/AKDSFramework/workflows/AKDSFramework/badge.svg)](https://github.com/theroyakash/AKDSFramework/actions)
[![Python3](https://img.shields.io/badge/python-3.8-blue.svg)](https://github.com/theroyakash/reddit-api)
[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/theroyakash/AKDSFramework/blob/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-theroyakash-red)](https://www.iamroyakash.com/contact)
[![GitHub license](https://img.shields.io/badge/Privacy-Policy-blue)](https://www.iamroyakash.com/privacy)

AKDSFramework is a Purely written in Python library containing implementations of various data structures.

Our Package will allow user to focus on developing algorithms and not worry about finding python-compatible implementations of classic data structures like linked list, heap and others.

# Useful links
- **Documentation** We've written a comprehensive documentation for our framework AKDSFramework. Have a look at it [here](https://github.iamroyakash.com/AKDSFramework-docs) and a read-the-docs version is also available [here](https://akdsframework.readthedocs.io/en/latest/)
- See what's in the **works** now [here](https://www.notion.so/theroyakash/8a9998cb8b7f4d318e05dfce28fbcfda?v=b8c3cf3084a8426394f7307a2005c945).

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
## Currnetly supporting APIs

| Supporting API                             | Scope                      |
|--------------------------------------------|----------------------------|
| Singly Linked List                         | Data Structures            |
| Graph                                      | Data Structures            |
| Priority Queues with heap                  | Data Structures            |
| Queues                                     | Data Structures            |
| Stacks                                     | Data Structures            |
| Graphs (Adjacency Matrix)                  | Graph Structures           |
| Graphs (Adjacency List)                    | Graph Structures           |
| BFS and DFS                                | Graph Algorithms           |
| Single Source Shortest paths               | Graph Algorithms           |
| Representing a graph with drawings         | Graph Algorithms           |
| Dictionary (Hash Table)                    | Data Structures            |
| Linear Search and Binary Search            | Search Algorithms          |
| Big O complexity analysis                  | General purpose Algorithms |
| Merge, Quick, Bubble, Insertion, Heap Sort | Sorting Algorithms         |

### Contributing
[![GitHub license](https://img.shields.io/badge/CONTRIBUTING-Welcome-blue)](https://github.com/theroyakash/AKDSFramework/pulls)

Contributions are welcome. Make PR or open a new issue with some idea.