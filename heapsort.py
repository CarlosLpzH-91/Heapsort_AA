


def heap_up(a, indx, length):
    root = indx
    left = 2 * indx + 1
    right = 2 * indx + 2

    if left < length and a[indx] < a[left]:
        root = left
    if right < length and a[root] < a[right]:
        root = right
    if root != indx:
        a[indx], a[root] = a[root], a[indx]

        heap_up(a, root, length)


def heap_sorting(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heap_up(a, i, n)

    for j in range(n - 1, 0, -1):
        a[j], a[0] = a[0], a[j]
        heap_up(a, 0, j)







