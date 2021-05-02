import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card(spades, 1)
        self.club = Card(clubs, 5)
    

    def card_value_equals_1 (self):
        self.assertEqual(1, self.ace.value)
    

    

