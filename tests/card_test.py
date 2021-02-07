import unittest
from src.card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card(1)