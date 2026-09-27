def insertion_sort(a):
    print("นายณัฐกรณ์ หนูวรรณ 6806021612428")
    print("Original :  [34, 8, 64, 51, 32, 21] Position Move")
    for p in range(1, len(a)):
        tmp = a[p]
        j = p
        m = 0
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
            m += 1
        a[j] = tmp
        print(f"After P = {p} {a} = {m} ")
    print(f"Result   :  {a}")
insertion_sort([34, 8, 64, 51, 32, 21])
