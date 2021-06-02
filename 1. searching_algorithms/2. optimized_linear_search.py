def linear_search(arr, key):
    n = len(arr)
    for i in range(n//2 + 1):  # One extra iteration
        if arr[i] == key:
            return i
        if arr[n-1-i] == key:
            return n-i-1
    return -1


def linear_search2(arr, key):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        if arr[left] == key:
            return left
        if arr[right] == key:
            return right
        left += 1
        right -= 1
    return -1


if __name__ == "__main__":
    arr = [55, -78, 88, 1, -50]
    print(linear_search(arr, 88))
    print(linear_search(arr, 100))
    arr = [55, -78, 88, 1, -50, 60]
    print(linear_search(arr, 88))
    print(linear_search(arr, 100))

    arr = [55, -78, 88, 1, -50]
    print(linear_search2(arr, 88))
    print(linear_search2(arr, 100))
    arr = [55, -78, 88, 1, -50, 60]
    print(linear_search2(arr, 88))
    print(linear_search2(arr, 100))
