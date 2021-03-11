<h1 align="center">
  <br>
  <a href="https://github.iamroyakash.com/AKDSFramework-docs"><img src="https://i.imgur.com/uDSHEhr.png" alt="AKDSFramework" width="800"></a>
  <br>
  AKDSFramework
  <br>
</h1>

AKDSFramework is a python Package for all your data structure and algorithm needs. AKDSFramework is a Purely written in Python library.

[![AKDSFramework Build Status](https://github.com/theroyakash/AKDSFramework/workflows/AKDSFramework/badge.svg)](https://github.com/theroyakash/AKDSFramework/actions)
[![Python3](https://img.shields.io/badge/python-3.9-blue.svg)](https://github.com/theroyakash/reddit-api)
[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/theroyakash/AKDSFramework/blob/master/LICENSE)
[![Discord Server](https://img.shields.io/badge/Support-theroyakash-red)](https://www.iamroyakash.com/contact)
[![GitHub license](https://img.shields.io/badge/Privacy-Policy-blue)](https://www.iamroyakash.com/privacy)

[View it on GitHub](https://github.com/theroyakash/AKDSFramework)

Our Package will allow user to focus on developing algorithms and not worry about finding python-compatible implementations of classic data structures like linked list, heap and others.

# Setup
- First download/clone this repo like git clone `https://github.com/theroyakash/AKDSFramework.git`
- Now uninstall if any previous version installed `pip3 uninstall AKDSFramework`
- Now install fresh on your machine `pip3 install -e AKDSFramework`

## Alternate installation
This is easier to install but a bit slower in the installation time.
`pip3 install https://github.com/theroyakash/AKDPRFramework/tarball/main`

## First code, Check the version
Now to check whether your installation is completed without error import AKDSFramework
```python
import AKDSFramework
print('AKDSFramework Version is --> ' + AKDSFramework.__version__)
```
### Example code creating Linked List
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

## Currently supporting APIs

| Supporting APIs                             | Scope                      |
|--------------------------------------------|----------------------------|
| [Singly Linked List](https://github.iamroyakash.com/AKDSFramework-docs/docs/linked-lists.html)                         | Data Structures            |
| [Graph](https://github.iamroyakash.com/AKDSFramework-docs/docs/graphs.html)                                      | Data Structures            |
| Priority Queues with [heap](https://github.iamroyakash.com/AKDSFramework-docs/docs/heaps.html)                  | Data Structures            |
| [Queues](https://github.iamroyakash.com/AKDSFramework-docs/docs/queue.html)                                     | Data Structures            |
| [Stacks](https://github.iamroyakash.com/AKDSFramework-docs/docs/stacks.html)                                     | Data Structures            |
| [Graphs](https://github.iamroyakash.com/AKDSFramework-docs/docs/graphs.html) (Adjacency Matrix)                  | Graph Structures           |
| [Graphs](https://github.iamroyakash.com/AKDSFramework-docs/docs/graphs.html) (Adjacency List)                    | Graph Structures           |
| [BFS and DFS](https://github.iamroyakash.com/AKDSFramework-docs/docs/graphs.html#bfs-dfs)                                | Graph Algorithms           |
| [Single Source Shortest paths](https://github.com/theroyakash/AKDSFramework/blob/main/AKDSFramework/applications/singlesourceshortestpath.py)               | Graph Algorithms           |
| [Representing a graph with drawings](https://github.iamroyakash.com/AKDSFramework-docs/docs/graphs.html#visualize-the-graph)         | Graph Algorithms           |
| Dictionary (Hash Table)                    | Data Structures            |
| Linear Search and Binary Search            | Search Algorithms          |
| [Big O complexity analysis](https://publications.iamroyakash.com/introducing-an-efficient-big-o-analyzer)                  | General purpose Algorithms |
| Merge, Quick, Bubble, Insertion, Heap [Sort](https://github.iamroyakash.com/AKDSFramework-docs/docs/sorting.html) | Sorting Algorithms         |

### License

AKDSFramework is &copy; 2020 by [theroyakash](https://www.iamroyakash.com) is distributed by an [MIT license](https://github.com/theroyakash/AKDSFramework/blob/main/LICENSE).

### Contributing
![GitHub license](https://img.shields.io/badge/CONTRIBUTING-Welcome-green)

When contributing to this repository, please first discuss the change you wish to make via issue or discussion,
email, or any other method with the owners of this repository before making a change. Get started in [our GitHub repo](https://github.com/theroyakash/AKDSFramework/).