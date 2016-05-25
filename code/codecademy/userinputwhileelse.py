from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You Lose")
