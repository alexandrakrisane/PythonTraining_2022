import random


def get_shuffled_cards():
    # card_suits_black = ['diamonds ♦', 'hearts ♥', 'spades ♠', 'clubs ♣']  # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode

    card_suits = ['diamonds ♦', 'hearts ♥', 'spades ♠', 'clubs ♣']
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = [(r, s) for r in card_ranks for s in card_suits]
    #print(f"New deck of {len(deck)} cards is created:\n {deck}")  # prints non shuffled deck of cards for testing purposes

    random.shuffle(deck)
    print(f"New deck of {len(deck)} cards is created and shuffled:\n {deck}")

    return deck


# print(get_shuffled_cards())
