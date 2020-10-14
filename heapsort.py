"""
Heap Sort Algorithm.

Creado el 09/10/2020 por Carlos A. López Herrera
"""


# Build the heap from the array.
def heap_up(array, index, length):
    root = index  # Set the index of the root.
    left = 2 * index + 1  # Set the index of the left child.
    right = 2 * index + 2  # Set the index of the right child.

    # if left child exists and it's bigger than the root,
    # then swap them.
    if left < length and array[index] < array[left]:
        root = left
    # if right child exists and it's bigger than the root,
    # then swap them.
    if right < length and array[root] < array[right]:
        root = right
    # if the index of root is different than the current index
    # then swap the values.
    if root != index:
        array[index], array[root] = array[root], array[index]

        # Recursive call on the new root.
        heap_up(array, root, length)


# Sort the root.
def heap_sorting(array):
    # Get the length of the array.
    n = len(array)

    # Apply the heap_up method on each root, from bottom to top.
    for i in range(n // 2 - 1, -1, -1):
        heap_up(array, i, n)

    # Subtract the max root, and re-apply the heap_up method to the remaining elements.
    for j in range(n - 1, 0, -1):
        array[j], array[0] = array[0], array[j]
        heap_up(array, 0, j)
