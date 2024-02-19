def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number: "))
even_nums = even_numbers(n)
print(*even_nums, sep=",")
