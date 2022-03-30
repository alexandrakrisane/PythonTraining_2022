import random


def get_shuffled_cards():
    # card_suits_white = ['diamonds \u2662', 'hearts \u2661', 'spades \u2664', 'clubs \u2667']
    # card_suits_bw = ['diamonds ♢', 'hearts ♡', 'spades ♠', 'clubs ♣']
    # card_suits_white = ['diamonds ♢', 'hearts ♡', 'spades ♤', 'clubs ♧']
    # card_suits_black = ['diamonds ♦', 'hearts ♥', 'spades ♠', 'clubs ♣']  # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode

    card_suits = ['diamonds ♦', 'hearts ♥', 'spades ♠', 'clubs ♣']
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = [(r, s) for r in card_ranks for s in card_suits]
    #print(f"New deck of {len(deck)} cards is created:\n {deck}")  # prints non shuffled deck of cards for testing purposes

    random.shuffle(deck)
    print(f"New deck of {len(deck)} cards is created and shuffled:\n {deck}")

    return deck


if __name__ == '__main__':
    print("This will run when shuffled_cards.py is called normally")
    #cards = get_shuffled_cards()
else:
    print("It was imported! My __main__ is", __name__)

# print(get_shuffled_cards())
