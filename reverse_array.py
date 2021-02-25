if __name__ == "__main__":
    arr = [2, 4, 6, 9, 8, 10, 3]
    arr_length = len(arr)
    for i in range(arr_length//2):
        j = arr_length - i-1
        arr[i], arr[j] = arr[j], arr[i]
    print(arr)
