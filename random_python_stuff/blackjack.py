import numpy as np

def blackjack():
    play_again = "y"
    player_wins, dealer_wins, ties = 0, 0, 0

    while (play_again == "y"):
        print("--------------Welcome to the Table--------------")

        print("--------------Player's turn--------------")
        player_card_one = np.random.randint(1, 12)
        print("Player Card One:", player_card_one)

        print("--------------Dealer's turn--------------")
        dealer_card_one = np.random.randint(1, 12)
        print("Dealer Card One:", dealer_card_one)

        print("--------------Player's turn--------------")
        sum_of_player_cards = player_card_one
        player_card_two = np.random.randint(1, 12)
        print("Player Card Two:", player_card_two)
        sum_of_player_cards += player_card_two
        print("Player Card Total:", sum_of_player_cards)

        if sum_of_player_cards < 21:
            dec = input("(h)it or (s)tand? ")
            while dec == "h" and sum_of_player_cards < 21:
                player_card = np.random.randint(1, 12)
                print("Player Card", player_card)
                sum_of_player_cards += player_card
                print("Player Card Total", sum_of_player_cards)
                if sum_of_player_cards >= 21:
                    break
                else:
                    dec = input("(h)it or (s)tand? ")

        sum_of_dealer_cards = dealer_card_one
        if sum_of_player_cards <= 21:
            print("--------------Dealer's turn--------------")
            while sum_of_dealer_cards <= 17:
                dealer_card = np.random.randint(1, 12)
                print("Dealer Card", dealer_card)
                sum_of_dealer_cards += dealer_card
                print("Dealer Card Total", sum_of_dealer_cards)
        if ((sum_of_dealer_cards > sum_of_player_cards) and sum_of_dealer_cards <=21):
            print("Dealer Wins!")
            dealer_wins += 1
        elif ((sum_of_player_cards > sum_of_dealer_cards) and sum_of_player_cards <= 21):
            print("Player Wins!")
            player_wins += 1
        elif (sum_of_dealer_cards > 21):
            print("Player Wins!")
            player_wins += 1
        elif (sum_of_player_cards > 21):
            print("Dealer Wins!")
            dealer_wins += 1
        else:
            print("Tie Game!")
            ties += 1
        play_again = input("Do you want to play again? (y)es or (n)o " )

    print("--------------Game Statistics--------------")
    print("Player Wins:", player_wins)
    print("Dealer Wins:", dealer_wins)
    print("Ties:", ties)
    
if __name__ == '__main__':
    blackjack()