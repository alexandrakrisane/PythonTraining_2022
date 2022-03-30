# 11 30.03.2022

import deck

cards = deck.Deck()
print('_' * 100)

cards.get_cards(count=1)

cards.get_cards(count=3)  #
cards.get_cards(count=1)
# cards.get_cards(count=8)  #
# cards.get_cards(count=8)
# cards.get_cards(count=1)

# print(cards.get_cards(count=1))

#
cards.back_into_deck(count=7)  # tries to remove elements from the list
cards.back_into_deck(count=2)  # removes elements from the list
cards.get_cards(count=62)
#
cards.all_cards_back_into_deck()
#
cards.get_cards(count=3)
# cards.print_used_cards()

