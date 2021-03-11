# Searching
Searching is available under AKDSFramework.applications.search module. This is AKDSFramework searching package. Implements Linear, Binary Search

## Binary search
`AKDSFramework.applications.search.binarysearch(array: list, target: any, require_sorting=False) → any`

Binary search implementation. Use only when your array is sorted. Pass in require_sorting as True to sort on the fly.

### Args:
- array (list): Search space
- target (any): Value of the target that you want to search

### Returns:
- True if element found else False

## Linear Search
`AKDSFramework.applications.search.linearsearch(array: list, target: any) → any`
Implementation of linear search. Use only when your array is not sorted. If you have a sorted array use binary search instead. Running time 𝑂(𝑁)

### Args:
- array (list): List of any data type
- target (any): Value of the target that you want to search

### Returns:
None if no element found or dictionary of {index, target} of the element where it’s found.