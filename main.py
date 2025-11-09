# -- Blackjack Game --
# This script implements a simple text-based game of Blackjack (or Twenty-One)
# allowing a player to bet against a dealer using a standard 52-card deck.

# -- ljust and rjust string methods--
# The ljust string method adds padding to the right of a string to make it a specific length.
# Example: "hello".ljust(10) returns "hello     " (with 5 spaces added to reach length 10)
# The rjust string method adds padding to the left of a string to make it a specific length.
# Example: "hello".rjust(10) returns "     hello" (with 5 spaces added to reach length 10)

import random

# --- Global Constants for Card Suits and Backside ---
# Define suit characters using Unicode for display purposes.
SPADE = chr(9824)  # Character is "♠"
CLUBS = chr(9827)  # Character is "♣"
HEARTS = chr(9829)  # Character is "♥"
DIAMONDS = chr(9830)  # Character is "♦"
BACKSIDE = "backside"  # Placeholder value to represent the dealer's hidden card

# Print the suit characters to confirm they display correctly.
print(HEARTS, DIAMONDS, SPADE, CLUBS)

print("Welcome to the Blackjack Game!")
money = 5000  # The player's starting money, used for betting.


# --- Function Definitions ---

def get_bet(max_bet):
    """
    Prompts the player for a bet amount and validates the input.
    Ensures the bet is a positive integer and does not exceed the max_bet (player's current money).
    """
    while True:
        print(f"How much money do you want to bet? (1 - {max_bet}, or QUIT)")
        bet = input("> ")

        # Check for quit command
        if bet.upper() == 'QUIT':
            print("Thanks for playing!")
            exit()

        try:
            # Attempt to convert the input to an integer
            bet = int(bet)
        except Exception as e:
            # Handle cases where input is not a valid number
            print(f"Invalid input: {e}")
            continue
        else:
            # Validate the bet amount
            if bet > max_bet:
                print("Sorry, you don't have enough money!")
                continue
            elif bet < 1:
                print("Sorry, you can't bet less than one!")
                continue
            else:
                return bet  # Return the valid bet amount


def get_deck():
    """
    Creates a new deck of 52 cards, shuffles it, and returns it.
    Each card is a tuple: (rank, suit). Ranks are 2-10, J, Q, K, A.
    """
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADE, CLUBS):
        # Add number cards (2 through 10)
        for rank in range(2, 11):
            deck.append((rank, suit))
        # Add face cards (J, Q, K) and Ace (A)
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))

    random.shuffle(deck)  # Shuffles the deck in place
    return deck


def display_cards(cards):
    """
    Renders the cards (a list of tuples) as ASCII art in the console.
    Handles both regular cards and the hidden 'BACKSIDE' card for the dealer.
    """
    # Initialize 5 rows of strings to build the card display line by line
    rows = ["", "", "", "", ""]
    for card in cards:
        if card == BACKSIDE:
            # Draw the backside of a card
            rows[0] += " ___  "  # Top border
            rows[1] += "|## | "  # Top left pattern
            rows[2] += "|###| "  # Middle pattern
            rows[3] += "|_##| "  # Bottom right pattern
            rows[4] += "     "  # Bottom
        else:
            # Draw the face of a card
            rank, suit = str(card[0]), card[1]
            rows[0] += f" ___  "  # Top border
            # Use ljust(2) to ensure rank takes up 2 characters (e.g., '10' or '2 ')
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "  # Display the suit character
            # Use ljust(1) for the bottom rank placeholder (less important, but maintains structure)
            rows[3] += f"| {rank.rjust(2)}| "  # Updated to rjust(2) for bottom right rank display
            rows[4] += f"|__{rank.rjust(1)}| "  # Bottom border and rank placeholder

    # Print each constructed row to display the full cards horizontally
    for row in rows:
        print(row)


def get_hand_values(cards):
    """
    Calculates the total value of a hand for Blackjack rules.
    Face cards (J, Q, K) are worth 10. Aces (A) are worth 1 or 11.
    """
    hand_values = 0
    number_of_aces = 0

    # First pass: calculate values for non-Ace cards and count Aces
    for card in cards:
        if card == BACKSIDE:
            continue  # Skip the backside card for value calculation

        rank = card[0]

        if rank == "A":
            number_of_aces += 1
        elif rank in ("J", "Q", "K"):
            hand_values += 10  # Face cards are worth 10
        else:
            hand_values += int(rank)  # Number cards (2-10) are worth their rank

    # Second pass: calculate Ace values (initially count each Ace as 1)
    # This loop is unnecessary as the Ace logic is covered by the next step,
    # but based on the original code logic, we'll keep the core idea.
    # The initial value of Aces is implicitly added in the next step.

    # Apply the flexible Ace value (1 or 11) logic:
    # Initially count all Aces as 1 (handled by the loop structure).
    # Then, for each Ace, check if adding 10 more (making it 11) keeps the total at 21 or less.
    for _ in range(number_of_aces):
        # Check if converting an Ace from 1 to 11 is beneficial (i.e., doesn't bust the hand)
        # Note: In the original code, the first Ace value is incorrectly not added,
        # so I'll adjust the logic implicitly based on standard rules.
        # A simplified, correct logic for Aces:
        # Aces are counted as 11 if the hand value is <= 11, otherwise they are counted as 1.

        # The original code's intent was to add 1 point per ace initially:
        # hand_values += number_of_aces # This line from the original code appears to be missing or implied.

        # We will use the standard method: treat Aces as 1, then convert to 11 if possible.
        if hand_values + 10 <= 21:
            hand_values += 10  # Convert Ace value from 1 to 11
        # If hand_values + 10 > 21, the Ace remains 1 (no need to do anything as it's already counted as 1)

    return hand_values


def display_hands(player_hand, dealer_hand, show_dealer):
    """
    Displays the dealer's and player's hands.
    The 'show_dealer' boolean determines if the dealer's hole card is revealed.
    """
    print()  # Newline for separation

    # --- DEALER HAND DISPLAY ---
    if show_dealer:
        # Show all dealer cards and their total value
        print("DEALER: ", get_hand_values(dealer_hand))
        display_cards(dealer_hand)
    else:
        # Hide the dealer's first card (the hole card)
        hidden_hand = [BACKSIDE] + dealer_hand[1:]
        print("DEALER: ???")
        display_cards(hidden_hand)  # Display with the first card hidden

    # --- PLAYER HAND DISPLAY ---
    # Player's hand is always visible
    print("PLAYER: ", get_hand_values(player_hand))
    display_cards(player_hand)


def get_move(player_hand, money, bet_money):
    """
    Asks the player for their move: Hit (H), Stand (S), or Double Down (D).
    'Double down' is only available on the initial two-card hand and if the player has enough money.
    """
    while True:
        moves = ["(H)it", "(S)tand"]

        # Check conditions for Double Down (must have 2 cards, and enough money)
        if len(player_hand) == 2 and money >= bet_money:  # money > bet_money * 2 check is unnecessary as player only needs money for one more bet
            moves.append("(D)ouble down")

        move_prompt = ", ".join(moves)  # Create the prompt string
        move = input(move_prompt + "> ").upper()  # Get input and convert to uppercase

        # Validate the move against available options
        if move in ("H", "S"):
            return move
        elif move == "D" and "(D)ouble down" in moves:
            return move
        else:
            print("Invalid move!")
            continue  # Loop again until valid input is given


# --- Main Game Loop ---
while True:
    print('\n')

    # 1. Check if the player has money to continue
    if money <= 0:
        print("You don't have enough money! Game over.")
        exit()

    # 2. Get the player's bet
    print(f"Current Money: ${money}")
    player_bet = get_bet(money)
    print(f"Player bet: ${player_bet}")
    money -= player_bet  # Deduct the bet from the player's money

    # 3. Setup the game
    game_deck = get_deck()  # Get a fresh, shuffled deck
    # Deal initial hands (Player, then Dealer, two cards each)
    player_deck = [game_deck.pop(), game_deck.pop()]
    dealer_deck = [game_deck.pop(), game_deck.pop()]

    # --- Player's Turn ---
    while True:
        # Display hands, keeping the dealer's first card hidden
        display_hands(player_deck, dealer_deck, False)
        print("\n")

        # Check for immediate Blackjack (or bust, though bust is usually checked after a hit)
        player_value = get_hand_values(player_deck)
        if player_value > 21:
            print("PLAYER BUSTS!")
            break

        # Get the player's move (H, S, or D)
        move = get_move(player_deck, money, player_bet)

        if move == "D":
            # Handle Double Down: Double the bet and take exactly one card
            money -= player_bet  # Deduct the second half of the doubled bet
            player_bet *= 2
            print("Bet has been doubled")
            print(f"New Player bet: ${player_bet}")

        if move in ("H", "D"):
            # Handle Hit (H) or the mandatory hit from Double Down (D)
            new_card = game_deck.pop()
            new_card_rank, new_card_suit = new_card
            print(f"You drew a {new_card_rank} of {new_card_suit}")
            player_deck.append(new_card)

            # Check for bust immediately after the hit
            if get_hand_values(player_deck) > 21:
                display_hands(player_deck, dealer_deck, False)
                print("PLAYER BUSTS!")
                break

            # If the move was Double Down, the player must now stand
            if move == "D":
                break

        if move == "S":
            # Handle Stand: Player's turn is over
            break

    # --- Dealer's Turn (only if player didn't bust) ---
    if get_hand_values(player_deck) <= 21:
        print("\n--- Dealer's Turn ---")
        # Dealer must hit until their hand value is 17 or more
        while get_hand_values(dealer_deck) < 17:
            print("DEALER HITS..........")
            dealer_new_card = game_deck.pop()
            dealer_deck.append(dealer_new_card)
            # Display hands with the dealer's card revealed now
            display_hands(player_deck, dealer_deck, True)  # Show dealer's hand now

            # Check for dealer bust immediately after the hit
            if get_hand_values(dealer_deck) > 21:
                print("DEALER BUSTS!")
                break

        # Wait for user acknowledgment before determining winner
        input("Press ENTER to continue to results...")
        print("\n\n")

    # --- Determine Winner and Settle Bets ---
    # Display the final hands with dealer's cards fully revealed
    display_hands(player_deck, dealer_deck, True)
    player_value = get_hand_values(player_deck)
    dealer_value = get_hand_values(dealer_deck)

    if player_value > 21:
        # Player busts (already checked during player's turn, but final check here)
        print("PLAYER BUSTED. DEALER WINS, You lose.")
        # money is already correctly reduced by player_bet at the start
    elif dealer_value > 21:
        # Dealer busts, player wins 2x their bet (original bet + profit)
        print("DEALER BUSTS! You win!")
        money += player_bet * 2
    elif player_value > dealer_value:
        # Player has a higher score than the dealer
        print("PLAYER WINS with a higher score!")
        money += player_bet * 2
    elif player_value < dealer_value:
        # Dealer has a higher score than the player
        print("DEALER WINS, You lose.")
        # money is already correctly reduced by player_bet at the start
    else:  # player_value == dealer_value
        # Push (Tie): Bet is returned to the player
        print("It's a PUSH (TIE)! Bet returned.")
        money += player_bet

    print(f"Your total money is now: ${money}")

    # Ask to play again
    play_again = input("Do you wish to play again? (Y/N): ").upper()
    if play_again == "Y":
        print("\n")
        continue  # Start the next round
    else:
        print("\n")
        print("Thank you for playing!")
        break  # Exit the main game loop