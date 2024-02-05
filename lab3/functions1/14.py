from hist import histogram
from sphere_v import sphere_volume
from gimiprime import filter_prime
from guess_game import guess_the_number
from spy_game import spy_game

# guess_the_number()
histogram([4, 9])
print(sphere_volume(radius = 5))
print(filter_prime(numbers=[1,2,34,5]))

print(spy_game([0,1,0, 7]))
print(spy_game([0,1,1, 7]))
print(spy_game([1,0,0, 7]))