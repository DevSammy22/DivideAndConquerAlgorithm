def quick_sort(arr):

    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (here I pick the middle one)
    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot] # Elements less than pivot
    middle = [x for x in arr if x == pivot] # Elements equal to pivot
    right = [x for x in arr if x > pivot] # Elements greater than pivot

    # Recursively sort the left and right parts, and combine them with the middle part
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)

    return left_sorted + middle + right_sorted


# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)

'''
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = []
    right = []
    middle = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)

'''