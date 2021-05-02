import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.ace = Card("spades", 1)
        self.club = Card("clubs", 5)
        self.diamond = Card("diamonds", 7)
        self.card_game1 = CardGame()
      

    
    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game1.check_for_ace(self.ace))
    
    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game1.check_for_ace(self.club))
    
    def test_highest_card1(self):
        card1 = self.club
        card2 = self.ace
        highest_card = self.card_game1.highest_card(card1, card2)
        self.assertEqual(card1, highest_card)
      
    def test_highest_card2(self):
        card1 = self.ace
        card2 = self.club
        highest_card = self.card_game1.highest_card(card1, card2)
        self.assertEqual(card2, highest_card)
    
    def test_cards_total_ace_and_club(self):
        cards = [self.ace, self.club]
        total_card = self.card_game1.cards_total(cards)
        self.assertEqual("You have a total of 6",total_card)
    
    def test_cards_total_club_and_diamond(self):
        cards = [self.club, self.diamond]
        total_card = self.card_game1.cards_total(cards)
        self.assertEqual("You have a total of 12",total_card)
    

    

