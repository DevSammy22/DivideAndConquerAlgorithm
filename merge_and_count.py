#mine
#Also, note that this is also similar with merge sort, you only need to remove all the inversion count and its relatives

def sort_and_count(A, n):
    if n == 1:
        return A, 0

    mid = n//2
    left_array = A[:mid]
    n_1 = len(left_array)
    right_array = A[mid:]
    n_2 = len(right_array)

    merge_left, left_inv_count = sort_and_count(left_array, n_1)
    merge_right, right_inv_count = sort_and_count(right_array, n_2)

    merge_result, result_inv = merge_and_count(merge_left, merge_right, n_1, n_2)
    total_inv_count = left_inv_count + right_inv_count + result_inv

    return merge_result, total_inv_count

def merge_and_count(left, right, n_1, n_2):
    i = j = 0
    count_inversion = 0
    merged_array = []

    while i < n_1 and j < n_2:
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            count_inversion = count_inversion + (n_1 - i)#I only checked this i
            j += 1

    while i < n_1:
        merged_array.append(left[i])
        i += 1

    while j < n_2:
        merged_array.append(right[j])
        j += 1

    return merged_array, count_inversion

'''
left = [3, 8, 12, 20, 32, 48]
n_1 = 6
right = [5, 7, 9, 25, 29]
n_2 = 5
'''
array = [3, 8, 12, 20, 32, 48, 5, 7, 9, 25, 29] #[9, 2, 5, 3, 2, 4, 10]
n= 11

result, count_inversion = sort_and_count(array, n)

#merge_result, count_inversion = merge_and_count(left, right, n_1, n_2)

print("merged array: ", result)
print("count inversion: ", count_inversion)
#print("merged result: ", result)



