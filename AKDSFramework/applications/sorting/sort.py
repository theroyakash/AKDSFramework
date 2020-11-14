from AKDSFramework.structure.heap import MinHeap
import random, sys

def bubblesort(array, vizualize=False, maintain_iter_dict=False):
    """
    Bubble sort algorithm, has worst case as performance O(n^2)
        Args:
            - array (list): List of elements
            - vizualize (bool): Marked as False by default. If you want to vizualize set this as True
    """

    def swap(pos1, pos2):
        array[pos1], array[pos2] = array[pos2], array[pos1]

    n = len(array)
    swapped = True

    iteration = 0

    if vizualize:
        print(f"Iteration {iteration}:", array)
    
    if maintain_iter_dict:
        iter_dict = {}
        iter_dict[f'{iteration}'] = array.copy()

    x = -1
    while swapped:
        swapped = False
        x += 1

        for i in range(1, n-x):
            if array[i - 1] > array[i]:
                swap(i-1, i)
                swapped = True

                if vizualize and maintain_iter_dict:
                    iteration += 1
                    print(f"Iteration {iteration}:", array)
                    iter_dict[f'{iteration}'] = array.copy()
                elif vizualize:
                    iteration += 1
                    print(f"Iteration {iteration}:", array)
                elif maintain_iter_dict:
                    iteration += 1
                    iter_dict[f'{iteration}'] = array.copy()

    if maintain_iter_dict:
        return array, iter_dict
    else:
        return array


def insertionsort(array, vizualize=False, maintain_iter_dict=False):
    """
    Insertion Sort method for sorting. Takes O(N^2) time in the worst case.
        Args:
            - array (list): List of elements
            - vizualize (bool): Marked as False by default. If you want to vizualize set this as True
    """
    iteration = 0
    if vizualize:
        print(f'Iteration {iteration}: {array}')

    if maintain_iter_dict:
        iter_dict = {}
        iter_dict[f'{iteration}'] = array.copy()

    for i in range(len(array)):
        cursor = array[i]
        position = i

        while position > 0 and array[position - 1] > cursor:
            array[position] = array[position - 1]
            position -= 1
        
        array[position] = cursor

        if vizualize:
            iteration += 1
            print(f"Iteration {iteration}: {array}")
        
        if maintain_iter_dict:
            iteration += 1
            iter_dict[f'{iteration}'] = array.copy()

    if maintain_iter_dict:
        return array, iter_dict
    else:
        return array


def heapsort(array, visualize=False):
    if visualize:
        iteration = 0

    ret = []

    mnheap = MinHeap(array)
    mnheap.build()
    
    while len(mnheap) >= 1:
        if len(mnheap) == 1:
            ret.append(mnheap[0])
            break

        # O(1) time access of minimum element
        root = mnheap.get_root()
        ret.append(root)
        # O(log n) operation
        mnheap.delete_root()  # Constant operation, deleting at the begining
        mnheap.build()        # O(log N)
        
        if visualize:
            print("-"*40)
            print(f'End of Iteration: {iteration}')
            print(f'Currently heap: {mnheap}')
            print(f'Our returning array: {ret}')
            
            iteration += 1
        
    return ret


def quicksort(array: list, inplace: bool) -> list:
    """
    Quick sort algorithm. Runs recursively
        Args:
            - array (list): List of data that you want sorted.
            - inplace (bool): Set this to true if you have space constraints
    """
    if not inplace:
        length = len(array)
        if length <= 1:
            return array
        else:
            # Choosing random element as pivot point ensures avarage case O(N log N) time
            randompivotindex = random.randint(0, len(array) - 1)
            pivot = array[randompivotindex]
            del array[randompivotindex]
        
        items_greater = []
        items_lesser = []

        for item in array:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lesser.append(item)

        return quicksort(items_lesser, False) + [pivot] + quicksort(items_greater, False)

    else:
        # # TODO: Implement the inplace version of the quick sort
        raise NotImplementedError

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              # The value from the left half has been used
              array[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                array[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1
    
    return array