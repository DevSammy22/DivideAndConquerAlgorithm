def partition(arr, low, high):
    # Pivot (Choosing the last element as the pivot)
    pivot = arr[high]
    # Pointer for the smaller element
    i = low - 1
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot element with the element at i+1 position
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(arr, low, high):
    if low < high:
        # Finding the partitioning index
        pivot_index = partition(arr, low, high)

        # Recursively sort the elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)



# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)