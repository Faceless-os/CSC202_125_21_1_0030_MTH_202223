# Number Guesing Game
player_health = 10
def game():
    def drink_potion():
        potion_strength = 2  
    print(player_health)
    drink_potion()
print(player_health)
game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]    
    print(new_enemy)
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
increase_enemies()
print(f"enemies outside function: {enemies}")
PI = 3.141
URL = "https://www.google.com"
TWITTER_HANDLE ="@Go_od_ness"
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer, turns):
    if guess > answer:
        print ("Too High")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
def set_difficulty():
    level = input("Choose level. Type 'easy' or 'hard':\n ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    #Guessing Numbers
def game():
    print("Welcome to the Number guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Oops, the correct answer is {answer}")
guess = int(input("Make a guess:\n"))
turns = set_difficulty()
print(f"You have {turns} attempts remaining to guess the number.")
guess = 0
while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
    elif guess != answer:
        print("Guess again.")
game()

