def reverse_number(n, cur=0):
    if n == 0:
        return cur
    return reverse_number(n // 10, cur * 10 + n % 10)
print(reverse_number(1243))