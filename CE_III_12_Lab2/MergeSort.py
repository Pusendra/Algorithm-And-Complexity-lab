

def merge_sort(array, a, r):
    
    if a < r:
        b = (a + r) // 2
        merge_sort(array, a, b)
        merge_sort(array, b + 1, r )
        merge(array, a, b, r)

def merge(array, a, mid, r):

    left_array = array[:mid]
    right_array = array[mid:]
    
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else:
            array[k] = right_array[j]
            j = j + 1
        k = k + 1

    while i < len(left_array):
        array[k] = left_array[i]
        i = i + 1
        k = k + 1

    while j < len(right_array):
        array[k] = right_array[j]
        j = j + 1
        k = k + 1
