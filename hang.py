import random

# List of predefined words for the game
WORDS = [
    "python", "hangman", "programming", "openai", "interface",
    "modular", "testing", "performance", "optimization", "visual"
]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""", """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""", """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""", """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""", """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""", """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""", """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

def get_random_word(word_list):
    """Return a random word from the word list."""
    return random.choice(word_list)

def display_game_state(hangman_pics, incorrect_guesses, correct_guesses, secret_word):
    """Display the current state of the game."""
    print(hangman_pics[len(incorrect_guesses)])
    print("\nIncorrect guesses: ", " ".join(incorrect_guesses))
    blanks = ["_"] * len(secret_word)
    
    for i in range(len(secret_word)):
        if secret_word[i] in correct_guesses:
            blanks[i] = secret_word[i]
    
    print(" ".join(blanks))

def get_guess(already_guessed):
    """Prompt the player for a guess, ensuring the input is valid."""
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else:
            return guess

def play_again():
    """Ask the player if they want to play again."""
    return input("Do you want to play again? (yes or no) ").lower().startswith('y')

def main():
    """Main function to run the Hangman game."""
    print("H A N G M A N")
    incorrect_guesses = []
    correct_guesses = []
    secret_word = get_random_word(WORDS)
    game_over = False

    while True:
        display_game_state(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)

        guess = get_guess(incorrect_guesses + correct_guesses)

        if guess in secret_word:
            correct_guesses.append(guess)
            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_guesses:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"Yes! The secret word is '{secret_word}'! You have won!")
                game_over = True
        else:
            incorrect_guesses.append(guess)
            if len(incorrect_guesses) == len(HANGMAN_PICS) - 1:
                display_game_state(HANGMAN_PICS, incorrect_guesses, correct_guesses, secret_word)
                print(f"You have run out of guesses! The word was '{secret_word}'.")
                game_over = True

        if game_over:
            if play_again():
                incorrect_guesses = []
                correct_guesses = []
                game_over = False
                secret_word = get_random_word(WORDS)
            else:
                break

if __name__ == "__main__":
    main()
p
