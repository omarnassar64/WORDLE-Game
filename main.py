import random
from logic import *
from grid import *

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# تحميل الكلمات من الملف
def load_words(file_path="words.txt"):
    with open(file_path, "r") as f:
        return f.read().splitlines()

words = load_words()
secretword = random.choice(words)
attempts = 6

print("Enter a word of five letters, YOU HAVE 6 ATTEMPTS\n")

for attempt in range(attempts):
    while True:
        the_guess = input().lower()
        if the_guess and len(the_guess) == 5:
            break
        else:
            print("The word must be 5 letters")

    result = check(the_guess, secretword, GREEN, YELLOW, RED, RESET)
    print_grid(result, attempts - attempt - 1)

    if the_guess == secretword:
        print("Correct! You guessed the word.")
        break
else:
    print(f"Game Over! The secret word was: {secretword}")
