import random

from shuffled_cards import get_shuffled_cards


class Deck:
    def __init__(self):
        self.available = get_shuffled_cards()  # shuffled deck is returned
        self.spent = []  # empty list

    def shuffle(self):
        random.shuffle(self.available)
        return self

    #
    # # gets some number(default 1) of cards from available
    # adds these cards to spent
    # returns these cards

    def get_cards(self, count=1):
        deck_size = 52  # for tests can be used 4
        if len(self.spent) + count <= deck_size:
            available = [c for c in self.available if c not in self.spent]  # list  -> to get unique cards from the list of available cards
            cards = random.sample(available, k=count)
            self.spent += cards
            print(f"Dealing...\n{self.spent}")
        elif len(self.spent) + count > deck_size:
            left = deck_size - len(self.spent)
            if left != 0:
                print(f'Not enough cards in the deck to deal, only {left} card(s) available')
            else:
                print('No cards in the deck to deal')
            pass
        return self

    def back_into_deck(self, count=1):
        if count <= len(self.spent):
            for i in range(count):
                self.spent.pop(0)  # removes first element of the list
            print(f"{count} card(s) have been put back into the deck")
            print(f'{len(self.spent)} card(s) remained in use:\n', self.spent)
        else:
            print("It is not possible to put more cards back into the deck than have actually been dealt - "
                  f"Only {len(self.spent)} card(s) can be put back into the deck")
            pass
        return self

    def all_cards_back_into_deck(self):
        print(f"All {len(self.spent)} dealt cards will be put back into the deck now")
        self.spent.clear()
        # print(f"empty list of dealt cards => {len(self.spent)} are currently in use")
        return self

    def print_used_cards(self):
        remains = len(self.available) - len(self.spent)
        print(f"Following cards are already dealt ({remains} cards remains in the deck): \n{self.spent}")
        return self
