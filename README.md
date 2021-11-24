<h1 align="center">
  <br>
  <a href="https://docs.akdsframework.theroyakash.com/"><img src="https://i.imgur.com/uDSHEhr.png" alt="AKDSFramework" width="800"></a>
  <br>
  AKDSFramework
  <br>
</h1>

<h4 align="center">Python Package for all your data structure and algorithm needs.</h4>

<p align="center">
  <a href="https://docs.akdsframework.theroyakash.com/">Getting started</a> •
  <a href="https://docs.akdsframework.theroyakash.com/docs/ds.html">Data Structures</a> •
  <a href="https://docs.akdsframework.theroyakash.com/docs/searching.html">Algorithms</a> •
  <a href="https://github.com/theroyakash/AKDSFramework/blob/main/LICENSE">License</a>
</p>

[![Build Status](https://github.com/theroyakash/AKDSFramework/workflows/AKDSFramework/badge.svg)](https://github.com/theroyakash/AKDSFramework/actions)
[![Python3](https://img.shields.io/badge/python-3.8-blue.svg)](https://github.com/theroyakash/reddit-api)
[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/theroyakash/AKDSFramework/blob/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-theroyakash-red)](https://www.theroyakash.com/contact)
[![GitHub license](https://img.shields.io/badge/Privacy-Policy-blue)](https://www.theroyakash.com/privacy)


AKDSFramework is a Purely written in Python library containing implementations of various data structures.

Our Package will allow user to focus on developing algorithms and not worry about finding python-compatible implementations of classic data structures like linked list, heap and others.

# Useful links
- **Documentation** We've written a comprehensive documentation for our framework AKDSFramework. Have a look at it [here](https://docs.akdsframework.theroyakash.com/).
- See what's in the **works** now [here](https://www.notion.so/theroyakash/8a9998cb8b7f4d318e05dfce28fbcfda?v=b8c3cf3084a8426394f7307a2005c945).

## Installation / Setup
I am working hard to make this framework available via PyPI. In the mean time do this
- `pip3 install https://github.com/theroyakash/AKDPRFramework/tarball/main`

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
| [Singly Linked List](https://docs.akdsframework.theroyakash.com/docs/linked-lists.html)                         | Data Structures            |
| [Graph](https://docs.akdsframework.theroyakash.com/docs/graphs.html)                                      | Data Structures            |
| Priority Queues with [heap](https://docs.akdsframework.theroyakash.com/docs/heaps.html)                  | Data Structures            |
| [Queues](https://docs.akdsframework.theroyakash.com/docs/queue.html)                                     | Data Structures            |
| [Stacks](https://docs.akdsframework.theroyakash.com/docs/stacks.html)                                     | Data Structures            |
| [Graphs](https://docs.akdsframework.theroyakash.com/docs/graphs.html) (Adjacency Matrix)                  | Graph Structures           |
| [Graphs](https://docs.akdsframework.theroyakash.com/docs/graphs.html) (Adjacency List)                    | Graph Structures           |
| [BFS and DFS](https://docs.akdsframework.theroyakash.com/docs/graphs.html#bfs-dfs)                                | Graph Algorithms           |
| [Single Source Shortest paths](https://github.com/theroyakash/AKDSFramework/blob/main/AKDSFramework/applications/singlesourceshortestpath.py)               | Graph Algorithms           |
| [Representing a graph with drawings](https://docs.akdsframework.theroyakash.com/docs/graphs.html#visualize-the-graph)         | Graph Algorithms           |
| Dictionary (Hash Table)                    | Data Structures            |
| Linear Search and Binary Search            | Search Algorithms          |
| [Big O complexity analysis](https://publications.theroyakash.com/introducing-an-efficient-big-o-analyzer)                  | General purpose Algorithms |
| Merge, Quick, Bubble, Insertion, Heap [Sort](https://docs.akdsframework.theroyakash.com/docs/sorting.html) | Sorting Algorithms         |

### Contributing
[![GitHub license](https://img.shields.io/badge/CONTRIBUTING-Welcome-blue)](https://github.com/theroyakash/AKDSFramework/pulls)

Contributions are welcome. Make PR or open a new issue with some idea.
