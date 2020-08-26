secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Correct, well done!")
        break           # terminates loop
else:                   # performed if loop not broken
    print(f"You failed. The correct number was {secret_number}.")