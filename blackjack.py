import random

def play_blackjack(player_wins, dealer_wins, player_money) :
    # Assign all possible values to represent the deck.
    deck_of_cards = [
            #   2  3  4  5  6  7  8  9  10  J   Q   K   A
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
                ]
    # Each time the game is played, the deck will be randomly shuffled.
    random.shuffle(deck_of_cards)

    dealer_hand = []
    player_hand = []
    hit_or_stand = 'hit'
    dealer_hit_or_stand = 'hit'

    # Will either be an L or a W
    player_round_result = ''
    player_money = player_money
    # How much or the total money can be used this round.
    round_money = int(input('How much money will you gamble this round? $'))


    # The player is given the first card, it is removed from the deck.
    player_hand.append(deck_of_cards.pop(0))
    # The dealer is give the second card, it is removed from the deck.
    dealer_hand.append(deck_of_cards.pop(0))
    player_hand.append(deck_of_cards.pop(0))
    dealer_hand.append(deck_of_cards.pop(0))

    # If the player has 21, Blackjack is printed. If they bust, that is printed.
    if sum(player_hand) == 21 :
        print("Blackjack!")
        hit_or_stand = 'blackjack'
    elif sum(player_hand) > 21 :
        print('You lose')
        hit_or_stand = 'over'
    else :
        # The player is shown their two cards and the dealer's second card (first card is covered)
        print('Your hand:', player_hand)
        print('Dealer hand: X',dealer_hand[1])

    # while loop that executes as long as the user wants to hit.
    while hit_or_stand == 'hit' :
        print('\n')
        # Player is asked whether to hit or stand.
        hit_or_stand = input('Hit or Stand: ').lower()
        # variable to represent the total amount in the players hand.
        sum_player_hand = sum(player_hand)

        # If a player hits, next card is removed from deck and added to players hand. Total of the hand is updated.
        if hit_or_stand == 'hit' :
            player_hand.append(deck_of_cards.pop(0))
            sum_player_hand = sum(player_hand)

            # Updated card appears for the player to see.
            print('Your hand: ', player_hand)
            print('Dealer hand: X', dealer_hand[1], '\n')

            # check score method is called. To determine if they have blackjack, busted, or can hit again.
            hit_or_stand = check_score(sum_player_hand)

        # If a player does not want to hit, and they input stand, they will get out of this loop.
        elif hit_or_stand == 'stand' :
            hit_or_stand = 'stand'

        # Players have to type hit or stand.
        else :
            print('Please type hit or stand. ')

    # Updated totals for both players and dealers hands.
    sum_player_hand = sum(player_hand)
    sum_dealer_hand = sum(dealer_hand)

    # My attempt at AI haha. Dealer has advantage in this game. If player has busted, they will stand.
    # If they have more points than the player, they will stand.
    # If they have 21, they will get blackjack.
    # If they have the same amount as the player, they will stand.
    # If the player has more than the dealer, the dealer will take the next card from the deck.
    # Check score method is called to check for blackjack, bust, or eligibility.
    while dealer_hit_or_stand == 'hit':

        if sum_player_hand > 21 :
            dealer_hit_or_stand = 'stand'
        elif sum_player_hand < sum_dealer_hand :
            dealer_hit_or_stand = 'stand'
        elif sum_dealer_hand == 21 :
            dealer_hit_or_stand = 'blackjack'
        elif sum_player_hand == sum_dealer_hand :
            dealer_hit_or_stand = 'stand'
        elif sum_player_hand > sum_dealer_hand :
            dealer_hand.append(deck_of_cards.pop(0))
            sum_dealer_hand = sum(dealer_hand)

            dealer_hit_or_stand = check_score(sum_dealer_hand)

    # Updated variables.
    sum_player_hand = sum(player_hand)
    sum_dealer_hand = sum(dealer_hand)

    # This determines who wins. and adds the necessary point to the win assignment.
    if hit_or_stand == 'blackjack' :
        # If the player get blacjack, they win. unless the dealer also get blackjack, then the dealer wins.
        if dealer_hit_or_stand == 'blackjack' :
            print('You got blackjack. But the dealer did too. You lose.')
            player_round_result = 'l'
            dealer_wins += 1
        else :
            print('You won. You got blackjack.')
            player_round_result = 'w'
            player_wins += 1
    elif hit_or_stand == 'over' :
        # If the user goes over, they lose.
        print('You went over. You lose.')
        player_round_result = 'l'
        dealer_wins += 1
    elif hit_or_stand == 'stand' :
        if sum_player_hand > sum_dealer_hand :
            # If the user has the higher card count they'll win (Which won't happen because the dealer is programmed to keep drawing until they are equal or higher.)
            print('You outplayed the dealer. You won.')
            player_round_result = 'w'
            player_wins += 1
        elif dealer_hit_or_stand == 'over' :
            # If the dealer busts, player wins.
            print('The dealer hit too many times. You won')
            player_round_result = 'w'
            player_wins += 1
        elif sum_player_hand < sum_dealer_hand :
            # If the dealer has the higher hand, they win.
            print('The dealer outplayed you. You lose')
            player_round_result = 'l'
            dealer_wins += 1
        else :
            # If it's a draw, dealer wins.
            print('Draw. You lose.')
            player_round_result = 'l'
            dealer_wins += 1
    else :
        # Just in case?
        print('System error.')


    # This calls the print_hands method. This displays all cards in each hands, and total count.
    print_hands(player_hand, dealer_hand, sum_player_hand, sum_dealer_hand)

    # This calls the winning_report method. Displays who wins.
    winning_report(player_wins, dealer_wins)

    # Calls the gambling function. Determines how much was made or lost this passed round.
    player_money = gambling_money(player_money, round_money, player_round_result)
    print('Round Money Remaining: $' + str(player_money))

    # If the player is out of money, they cannot return to the table.
    if player_money > 0 :
        play_again(player_wins, dealer_wins, player_money)
    else :
        print('Insufficient funds. Please come back another time.')

    # Play again function. If they want to try the dealer again.

     

# Gambling fuction will adjust money based on winning or losing.
def gambling_money(player_money, round_money, player_round_result) :
    if player_round_result == 'w' :
        output = round_money + player_money
        return output
    elif player_round_result == 'l' :
        output = player_money - round_money
        return output

# Check score. if score is 21 = assigns value to blackjack
# over 21 - bust.
# under 21, allows them to hit or stand.
def check_score(sum_player_hand) :
    if sum_player_hand == 21 :
        result = 'blackjack'
    elif sum_player_hand > 21 :
        result = 'over'
    else :
        result = 'hit'
    return result

# Method to reduce printing
def print_hands(player_hand, dealer_hand, sum_player_hand, sum_dealer_hand) :
    output = print('Your hand: ', player_hand, 'Total:',sum_player_hand, '\n', 'Dealer hand: ', dealer_hand, 'Total:', sum_dealer_hand)
    return output

# Method to reduce printing.
def winning_report(player_wins, dealer_wins) :
    output = print('You have won:', player_wins, 'times\n', 'Dealer has won:', dealer_wins, 'times\n')
    return output

# Determine if another game needs to be played.
def play_again(player_wins, dealer_wins, player_money) :
    again = input('Do you want to try again? (yes/no) ').lower()
    print('\n')
    if again == 'yes' :
        play_blackjack(player_wins, dealer_wins, player_money)
    else:
        pass



# Ask the user if they want to play.
start_up = input('Do you want to play Blackjack? (yes/no) ').lower()
print('\n')

# If the user inputs yes, assign the win values to 0 and call the blackjack function.
if start_up == 'yes' :
    player_money = int(input("How much money are you bringing to the table? $"))
    dealer_wins = 0
    player_wins = 0
    play_blackjack(player_wins, dealer_wins, player_money)
# If they don't input 'yes', nothing will happen.
else:
    pass