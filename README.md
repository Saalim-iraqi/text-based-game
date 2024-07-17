# Hangman Game

This is a simple text-based implementation of the classic Hangman game in Python. Players try to guess a hidden word by suggesting letters within a certain number of attempts.

## Features

- A list of predefined words for the game.
- Visual representation of the hangman at various stages.
- Tracks correct and incorrect guesses.
- Displays progress and remaining attempts after each guess.
- Handles invalid inputs gracefully.
- Option to play again after the game ends.

## Requirements

- Python 3.x

## How to Play

1. Run the script using Python.
2. The game will randomly select a word from the predefined list.
3. Players will be prompted to guess one letter at a time.
4. Correct guesses will be revealed in the word.
5. Incorrect guesses will add a part to the hangman.
6. The game continues until the player either guesses the word or runs out of attempts.
7. After the game ends, the player will be asked if they want to play again.

## How to Run

1. Ensure you have Python 3.x installed on your machine.
2. Download or clone this repository.
3. Navigate to the directory containing the script.
4. Run the script using the command:
   ```sh
   python hangman.py
   ```

## Code Structure

- `WORDS`: A list of predefined words for the game.
- `HANGMAN_PICS`: A list of strings representing the hangman at various stages.
- `get_random_word(word_list)`: Selects a random word from the given list.
- `display_game_state(hangman_pics, incorrect_guesses, correct_guesses, secret_word)`: Displays the current state of the game.
- `get_guess(already_guessed)`: Prompts the player for a guess and ensures it's valid.
- `play_again()`: Asks the player if they want to play again.
- `main()`: The main function that contains the game loop and controls the game flow.

## Example Output

```
H A N G M A N

  +---+
  |   |
      |
      |
      |
      |
=======

Incorrect guesses: 

_ _ _ _ _ _ _

Guess a letter: a

  +---+
  |   |
      |
      |
      |
      |
=======

Incorrect guesses: a

_ _ _ _ _ _ _

Guess a letter: e
...
```

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## Author

Developed by Mohammad Saalim Iraqi
