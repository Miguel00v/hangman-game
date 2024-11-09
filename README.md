# Hangman Game

The **Hangman Game** is a simple application built with Python and Flask, where the user attempts to guess a secret word, one letter at a time. With each incorrect guess, the number of attempts decreases, and the game continues until the user either guesses the word or runs out of attempts.

## Technologies

- **Python**: The programming language used to build the game logic.
- **Flask**: A lightweight web framework used to build the application.
- **HTML/CSS**: Used to construct the web pages and user interface.

## Features

- The game randomly selects a word from a predefined list of words.
- The user can try to guess the word one letter at a time.
- The game provides hints (clues) about the word.
- The player can try to guess the entire word at once.
- The game ends when the player guesses the word correctly or runs out of attempts.

## How to Play

1. Access the application in your browser.
2. The homepage will provide a clue about the secret word.
3. Start guessing the letters.
4. With each incorrect guess, the number of remaining attempts will decrease.
5. If you guess all the letters or the full word correctly, you win! Otherwise, the game ends when you run out of attempts.

## Installation

### Prerequisites

Before running the project, ensure that you have Python installed on your machine. You can verify this by running:

```bash
python --version
