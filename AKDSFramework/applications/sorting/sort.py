def bubblesort(array, vizualize=False):
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

    x = -1
    while swapped:
        swapped = False
        x += 1

        for i in range(1, n-x):
            if array[i - 1] > array[i]:
                swap(i-1, i)
                swapped = True
                if vizualize:
                    iteration += 1
                    print(f"Iteration {iteration}:", array)
    return array


def insertionsort(array, vizualize=False):
    """
    Insertion Sort method for sorting. Takes O(N^2) time in the worst case.
        Args:
            - array (list): List of elements
            - vizualize (bool): Marked as False by default. If you want to vizualize set this as True
    """
    iteration = 0
    if vizualize:
        print(f'Iteration {iteration}: {array}')

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

    return array
