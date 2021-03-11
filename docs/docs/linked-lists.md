# Linked List

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
