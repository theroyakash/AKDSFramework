# Heaps
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
```python
print(mxheap)
```

This will return `[2744, 1331, 2197, 729, 1000, 1728, 343, 512, 64, 8, 125, 1, 216, 27, 12, 4]` and you also have the ability to see the heap printed prettyly by using prettyprint() method.

```py
mxheap.prettyprint()
```