import unittest

from src.card_game import CardGame
from src.card import Card


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('hearts', 1)
        self.card2 = Card('spades', 2)
        self.card3 = Card('spades', 3)
        self.cardGame1 = CardGame()
        
    def test_for_ace(self):
        self.assertTrue(self.cardGame1.check_for_ace(self.card1))

    def test_for_ace__no_ace(self):
        self.assertFalse(self.cardGame1.check_for_ace(self.card2))
    
    def test_highest_card(self):
        self.assertEqual(self.card3, self.cardGame1.highest_card(self.card3, self.card1))
    
    def test_highest_card__fail(self):
        self.assertEqual(self.card3, self.cardGame1.highest_card(self.card1, self.card3))

    def test_cards_list_length(self):
        self.cardGame1.add_card(self.card1)
        self.assertEqual(1, self.cardGame1.card_count())
    
    def test_cards_total(self):
        self.cardGame1.add_card(self.card1)
        self.assertEqual("You have a total of 1", self.cardGame1.cards_total())

