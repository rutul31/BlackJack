# Blackjack Game

## Overview

This Python script implements a simple text-based Blackjack game. Players can place bets, receive cards, and make decisions to either hit or stay. The game includes a basic structure for a player, dealer, and deck of cards.

## Features

- **Card Representation:** The game uses a Card class to represent each card, with suits, ranks, and values.
- **Deck Management:** A Deck class manages the deck of cards, including shuffling and dealing.
- **Player Interaction:** Players can place bets, receive initial cards, and decide whether to hit or stay.
- **Dealer Logic:** The dealer follows a basic logic for playing, revealing the hidden card and making decisions accordingly.
- **Game Loop:** The game includes a loop for playing multiple rounds until the player decides to quit.

## Usage

1. **Run the Script:**
    ```bash
    python blackjack_game.py
    ```

2. **Place Your Bet:**
    - Enter the amount you want to bet.

3. **Gameplay:**
    - Follow the on-screen instructions to hit or stay.
    - The game will determine the winner based on Blackjack rules.

4. **Play Again:**
    - After each round, you can choose to play again or exit the game.

## Classes

### 1. Card Class
Represents a playing card with suit, rank, and value.

### 2. Deck Class
Manages a deck of cards, including shuffling and dealing.

### 3. Player Class
Represents a player with a name, bank balance, and methods for placing bets and managing cards.

### 4. Dealer Class
Represents the dealer with methods for managing cards and making decisions.

## Important Notes

- The game is a text-based implementation and does not have a graphical interface.
- Make sure to input valid choices during gameplay.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
