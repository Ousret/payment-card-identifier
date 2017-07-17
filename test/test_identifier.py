from unittest import TestCase, main
from payment_card_identifier.identifier import CardIdentifier
from payment_card_identifier.card import *


class TestCardIdentifier(TestCase):

    def test_visa_identifier(self):

        self.assertIsInstance(CardIdentifier.from_numbers('4532040524589053'), VISA)
        self.assertIsInstance(CardIdentifier.from_numbers('4024007190021666'), VISA)
        self.assertIsInstance(CardIdentifier.from_numbers('4485332542643260'), VISA)
        self.assertIsInstance(CardIdentifier.from_numbers('4716737564983025'), VISA)
        self.assertIsInstance(CardIdentifier.from_numbers('4532725361000038'), VISA)

        visa_card_numbers = '4532725361000038'

        for i in range(16, 0):
            if i > 0:
                self.assertIsNone(CardIdentifier.from_numbers(visa_card_numbers[i:]))
            else:
                self.assertIsNotNone(CardIdentifier.from_numbers(visa_card_numbers[i:]))

    def test_master_card_identifier(self):

        self.assertIsInstance(CardIdentifier.from_numbers('5550748741608464'), MasterCard)
        self.assertIsInstance(CardIdentifier.from_numbers('5202921902107780'), MasterCard)
        self.assertIsInstance(CardIdentifier.from_numbers('5462883565951364'), MasterCard)
        self.assertIsInstance(CardIdentifier.from_numbers('5322546131700355'), MasterCard)
        self.assertIsInstance(CardIdentifier.from_numbers('5319257079449071'), MasterCard)

    def test_amex_identifier(self):

        self.assertIsInstance(CardIdentifier.from_numbers('344539822519759'), Amex)
        self.assertIsInstance(CardIdentifier.from_numbers('372916735144419'), Amex)
        self.assertIsInstance(CardIdentifier.from_numbers('371200898558785'), Amex)
        self.assertIsInstance(CardIdentifier.from_numbers('343431456392573'), Amex)
        self.assertIsInstance(CardIdentifier.from_numbers('345697085612841'), Amex)

    def test_unknown_sequence_identifier(self):

        self.assertIsNone(CardIdentifier.from_numbers('0197287427'))
        self.assertIsNone(CardIdentifier.from_numbers('ABCHDKQDJ'))

if __name__ == '__main__':
    main()