import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame("check ace")
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Hearts", 2)
        self.cards = [self.card1, self.card2]   

    def test_check_for_ace(self):
        self.assertEqual(2, self.card2.value)
     
    def test_highest_card(self):
        highest_card_result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(2, highest_card_result.value)

    def test_cards_total(self):
        cards_total_result = self.card_game.cards_total(self.cards)
        self.assertEqual('You have a total of 3', cards_total_result)
        