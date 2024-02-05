import random

def guess_the_number():

    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    num_guesses = 0
  
    while True:
      num_guesses += 1
      print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
      print("Take a guess.")
  
      guess = int(input())
  
      if guess == number:
        print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
        break
      elif guess < number:
        print("Your guess is too low.")
      else:
        print("Your guess is too high.")
      
    return 0