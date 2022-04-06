"""
Direct Access Array Sort
"""

def direct_access_sort(arr):
    """
    Sort arr assuming items have distict non-negative keys
    """
    u = 1 + max([x for x in arr])
    daa = [None] * u
    for x in arr:
        daa[x] = x
    i = 0
    for key in range(u):
        if daa[key] is not None:
            arr[i] = daa[key]
            i += 1


if __name__ == "__main__":
    ar = [3, 1, 5, 6, 9, 21]
    direct_access_sort(ar)
    print(ar)
