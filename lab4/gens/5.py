def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test the countdown generator
for num in countdown(5):
    print(num)
