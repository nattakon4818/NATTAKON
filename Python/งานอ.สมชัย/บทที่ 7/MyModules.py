def sum_number(start = 1, end = 10):
    sum = 0
    for n in range(start, end + 1):
        sum += n
    return(sum)

def factorial1(num):
    if num > 1:
        return(num * factorial1(num - 1))
    else:
        return(1)

def draw_triangle(ch , num):
    for n in range(1, num + 1):
        print(ch * n)