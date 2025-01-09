import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return cards[random.randint(0, len(cards) - 1)]

def calculate_total(hand):
    total = sum(hand)
    if 11 in hand and total > 21:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def game():
    your_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    print(f"Computer's cards: [{computer_cards[0]}, ?]\n")

    hit = "yes"
    while calculate_total(your_cards) <= 21 and hit =="yes":
        hit = input("Do you want to hit? Type 'yes' or 'no': ").lower()
        if hit == "yes":
            your_cards.append(deal_card())
            print(f"Your cards: {your_cards}, current score: {calculate_total(your_cards)}")

    if calculate_total(your_cards) > 21:
        print("YOU LOSE! You went over 21.\n")
        return

    while calculate_total(computer_cards) < 17:
        computer_cards.append(deal_card())

  
    your_total = calculate_total(your_cards)
    computer_total = calculate_total(computer_cards)

    print(f"Your final hand: {your_cards}, final score: {your_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}\n")

    if computer_total > 21:
        print("YOU WIN! The computer went over 21.\n")
    elif your_total > computer_total:
        print("YOU WIN!\n")
    elif your_total < computer_total:
        print("YOU LOSE!\n")
    else:
        print("IT'S A TIE!\n")

def blackjack():
    play = input("Do you want to play Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        print(art.logo)
    while play == "y":
        game()
        play = input("Do you want to play again? Type 'y' or 'n': ").lower()
        if play == "y":
            print("\n" + "-" * 50 + "\n")

blackjack()
