def bubble_sort(arr):
    print("นายณัฐกรณ์ หนูวรรณ 6806021612428")
    print(f"Original, arr = [5, 1, 4, 2, 8]")
    n = len(arr)
    for i in range(n - 1):
        last_index = n - 1 - i
        for j in range(last_index):
            if arr[j] > arr[j + 1]:
                print(f"Swap  {arr[j]} and  {arr[j + 1]}")
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print(f"For loop i = {i}  arr = {arr}")
    print(f"For loop i = {n - 1}  arr = {arr}")
    print(f"Result   :              {arr}")
bubble_sort([5, 1, 4, 2, 8])
