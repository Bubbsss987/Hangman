import random
fruits = ["apple","banana","watermelon","tomato","coconut","lemon","blueberry","dates","orange","papaya"]
word = random.choice(fruits)
word_letters = set(word)
guessed_letters = set()
hangman_stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]
lives = len(hangman_stages)-1
print("Welcome to Hangman!")

while len(word_letters)>0 and lives > 0:
    print(hangman_stages[lives])
    display_letters = [letter if letter in guessed_letters else '_ ' for letter in word]
    print("Current word: ","".join(display_letters))
    print("Lives left: ", lives)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter!")
    elif guess in word_letters:
        word_letters.remove(guess)
        guessed_letters.add(guess)
        print("Good Guess!!")
    else:
        lives-=1
        guessed_letters.add(guess)
        print("Wrong Guess!!")
print("\n --Game Over--")
print(hangman_stages[lives])
if lives == 0:
    print("You lost the game! The word was: ", word)
else:
    print("Congratulations!! You won")

