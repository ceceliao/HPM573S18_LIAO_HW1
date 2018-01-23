def sumAll(n):
    sum_all = 0
    for i in range(1, n+1):
        sum_all = sum_all + i
    return sum_all

print(sumAll(100))

def sum_rec(n):
    if n ==1:
        return 1
    else:
        return n + sum_rec(n-1)

print(sum_rec(100))
