def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    arr = [55, -78, 88, 1, -50]
    print(linear_search(arr, 88))
    print(linear_search(arr, 100))
