import random

def guess_the_number():
    print("Hello !   What is your name?")
    name = input().strip()
    print("Well, {}, I am thinking of a number between 1 and 20".format(name))

    number_to_guess = random.randint(1, 20)
    number_of_guesses = 0

    while True:
        print("Take a guess")
        guess = int(input().strip())
        number_of_guesses += 1

        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print("Good job, {}! You guessed my number in {} guesses".format(name, number_of_guesses))
            break

print(guess_the_number())