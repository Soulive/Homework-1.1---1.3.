# Casino-Game

guess = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
secret = "7"

game = "Can you guess the correct number from 1 to 10?"

print(game)
guess = int(input())

if guess < 7:
    print("Too bad.")
elif guess > 7:
    print("Too bad.")
elif guess == 7:
    print("Congratulation! You guessed right!")
if not guess < 10:
    print("Your entered number is higher than 10. Please choose a number between 1 to 10")
else: "The system couldn´t recognize your input. Please choose a number between 1 to 10"



