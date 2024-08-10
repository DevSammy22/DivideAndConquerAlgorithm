def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]

    return i

def quick_select(arr, left, right, k):
    if len(arr) <= 1:
        return arr
    # Use the partition function to put the pivot in its correct position
    pivot_index = partition(arr, left, right)
    # If the pivot is in the position we're looking for, return it
    if k == pivot_index:
        return arr[k]
    # If the desired index k is less than the pivot index, search in the left part
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    # If the desired index k is less than the pivot index, search in the left part
    else:
        return quick_select(arr, pivot_index + 1, right, k)


# Example usage:
arr = [6, 2, 8, 1, 5, 4]
k = 3  # We want to find the 2nd smallest element (index 1)
result = quick_select(arr, 0, len(arr) - 1, k -1)
print("The 2nd smallest element is:", result)