# from lab3.functions1 import filter_prime
import sys
sys.path.insert(1, '../pp2/lab3/functions1')

from gimiprime import filter_prime

numbers = list(range(20))

primes = list(filter(lambda x: filter_prime([x]), numbers))
print(primes)