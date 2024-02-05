from functions1.gimiprime import filter_prime

numbers = list(range(20))

primes = list(filter(lambda x: filter_prime([x]), numbers))
print(primes)