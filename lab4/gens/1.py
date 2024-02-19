def square_generator(N):
  for i in range(1, N + 1):
    yield i * i

for square in square_generator(5):
  print(square)
