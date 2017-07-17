from unittest import TestCase, main
from payment_card_identifier.card import *


class TestCard(TestCase):

    def test_card_json(self):

        my_card = VISA('4532040524589053')

        self.assertIsNotNone(my_card.json)
        self.assertIsInstance(my_card.json, str)

    def test_card_base_properties(self):

        my_card = VISA('4532040524589053')

        self.assertEqual(my_card.name, 'VISA')
        self.assertEqual(my_card.is_valid, True)

if __name__ == '__main__':
    main()
