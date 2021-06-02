def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = left + (right - left)//2

        if arr[mid] == key:
            return mid

        if key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(arr, left, right, key):
    if left > right:
        return -1

    mid = left + (right-left)//2
    if arr[mid] == key:
        return mid

    if key < arr[mid]:
        return binary_search_recursive(arr, left, mid-1, key)

    return binary_search_recursive(arr, mid+1, right, key)


if __name__ == "__main__":
    arr = [55, -78, 88, 1, -50]
    print(binary_search(arr, 88))
    print(binary_search(arr, 100))
    arr = [55, -78, 88, 1, -50, 60]
    print(binary_search(arr, 88))
    print(binary_search(arr, 100))

    arr = [55, -78, 88, 1, -50]
    print(binary_search_recursive(arr, 0, len(arr)-1, 88))
    print(binary_search_recursive(arr, 0, len(arr)-1, 100))
    arr = [55, -78, 88, 1, -50, 60]
    print(binary_search_recursive(arr, 0, len(arr)-1, 88))
    print(binary_search_recursive(arr, 0, len(arr)-1, 100))
