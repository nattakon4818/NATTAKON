def selection_sort(arr):
    print("นายณัฐกรณ์ หนูวรรณ 6806021612428")
    print("Original :    [64, 25, 12, 22, 11]     min_idx   swap")
    n = len(arr)
    for i in range(n):
        min_idx = i
        swap = 0
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            temp = arr[i]
            arr[i] = arr[min_idx]
            arr[min_idx] = temp
            swap = 1
        last_j = j if i < n - 1 else i
        print(f"For i = {i} , j = {last_j} {arr}   {min_idx}         {swap}")
    print(f"Result   :  {arr}")
selection_sort([64, 25, 12, 22, 11])
