# 🃏 PyBlackjack - Console Blackjack Game

A simple, text-based implementation of the classic casino game **Blackjack** (also known as Twenty-One) written in pure Python. This project features ASCII art for card visualization, realistic betting mechanics, and implements core game actions like Hit, Stand, and Double Down.

## ✨ Features

* **ASCII Card Display:** Uses Unicode suit characters (♠, ♣, ♥, ♦) and string methods (`ljust`, `rjust`) to render cards cleanly in the console.
* **Betting System:** Players start with $5000 and can bet, win, lose, or get their bet returned on a 'Push' (tie).
* **Core Blackjack Logic:** Correctly handles card values, including the flexible **Ace** (1 or 11) rule, and enforces dealer rules (must hit on 16 or less, stand on 17 or more).
* **Game Moves:** Supports **Hit**, **Stand**, and **Double Down** (available on the initial two cards).

## 🚀 How to Run

### Prerequisites

You need **Python 3.x** installed on your system.

### Steps

1.  **Clone the Repository (or download the file):**
    ```bash
    git clone [https://github.com/YourUsername/Console-Blackjack.git](https://github.com/YourUsername/Console-Blackjack.git)
    cd Console-Blackjack
    ```
2.  **Run the Game:**
    Assuming your file is named `blackjack_game.py`:
    ```bash
    python blackjack_game.py
    ```

## 🎮 How to Play

The game follows standard Blackjack rules.

1.  **Start:** You begin with **$5000**.
2.  **Bet:** Enter the amount you wish to bet when prompted.
3.  **Hands Dealt:** You and the dealer are dealt two cards. One of the dealer's cards (the hole card) is hidden.
4.  **Your Turn:** Based on your hand total, you can choose a move:
    * **(H)it:** Take one more card.
    * **(S)tand:** Keep your current hand and end your turn.
    * **(D)ouble Down:** (Available only on the first two cards) Double your bet, take exactly one card, and then automatically stand.
5.  **Dealer's Turn:** If you don't bust, the dealer reveals their hidden card and continues to draw cards until their hand value is **17 or greater**.
6.  **Results:** The winner is determined, and bets are settled. The goal is to get a score closer to 21 than the dealer without going over 21.

## ⚙️ Project Structure

The entire game logic is contained within a single file, which makes it an excellent example for learning Python functions and control flow.

* `get_bet(max_bet)`: Handles user input for betting and validation.
* `get_deck()`: Creates and shuffles a standard 52-card deck.
* `display_cards(cards)`: **Key function** for rendering the ASCII art for the cards.
* `get_hand_values(cards)`: Calculates the score of a hand, handling Ace logic (1 or 11).
* `display_hands(...)`: Controls how the player and dealer hands are shown, including hiding the dealer's hole card.
* `get_move(...)`: Prompts the player for their action (Hit, Stand, Double Down).
* `Main Game Loop`: Manages the flow of the game, dealing cards, executing turns, and settling bets.

## 💡 Code Highlights

This project demonstrates effective use of Python's **string manipulation** for console output, specifically:

```python
# The ljust method pads the string on the right:
"2".ljust(2)  # returns "2 "
# Used for the top-left rank display on the card.
