import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card("spades", 1)
        self.club = Card("clubs", 5)
    

    def test_check_for_ace(self):
        self.assertEqual(True, self.ace.value)
    
    # def test_check_for_ace_false(self):
    #     self.assertEqual(False, self.club.value)

    def test_highest_card1(self):
        card1 = self.club.value
        card2 = self.ace.value
        self.assertEqual(card1, def_highest_card(card1,card2) )



    

    

