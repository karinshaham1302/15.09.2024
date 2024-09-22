import random

random.random
LUCKY_NUMBER: int = random.randint(1, 100)
counter: int = 0
guess: int = 0

while True:
    guess = int(input('guess a number between 0-100:'))
    counter += 1
    if guess == LUCKY_NUMBER:
        break
    if guess > LUCKY_NUMBER:
        print('guess lower')
    else:
        print('guess higher')

print(f'correct! number of attempts{counter}')

# stop
