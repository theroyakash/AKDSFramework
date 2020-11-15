"""
AKDSFramework searching package. Implements Linear, Binary Search
"""

def linearsearch(array: list, target: any) -> any:
    r"""
    Implementation of linear search. Use only when your array is not sorted. If you have a sorted array use binary search instead.Running time :math:`O(N)`
        Args:
            - ``array`` (list): List of any data type
            - ``target`` (any): Value of the target that you want to search
        Returns:
            None if no element found or dictionary of {index, target} of the element where it's found
    """
    for i in range(len(array)):
        if array[i] == target:
            return {
                "index": i,
                "target": target
            }
    return None

def binarysearch(array: list, target: any, require_sorting=False) -> any:
    r"""
    Binary search implementation. Use only when your array is sorted. Pass in ``require_sorting`` as ``True`` to sort on the fly.
        Args:
            - ``array`` (list): Search space
            - ``target`` (any): Value of the target that you want to search
        Returns:
            ``True`` if element found else ``False``
    """

    if require_sorting:
        array.sort()

    if len(array) == 0:
        return False

    mid_point = len(array) // 2 
    
    if array[mid_point] == target:
        return True
    elif array[mid_point] < target:
        return binarysearch(array[mid_point + 1:], target)
    else:
        return binarysearch(array[:mid_point], target)
