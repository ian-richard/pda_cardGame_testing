class CardGame:


  def __init__(self):
    self.cards = []


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
        return card1
    else:
        return card2
  
  def add_card(self, card):
    self.cards.append(card)

  def card_count(self):
    return len(self.cards)


  def cards_total(self):
    total = 0
    for card in self.cards:
      total += card.value
      return 'You have a total of {}'.format(total)
  