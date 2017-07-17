from payment_card_identifier import card
from payment_card_identifier.card import IllegalPaymentCardNumbers


class CardIdentifier:

    @staticmethod
    def from_numbers(numbers):
        """
        Try to identify and create instance of card.
        :param numbers: Card numbers
        :return: VISA, MasterCard, Amex instance or List of match
        :rtype: card.PaymentCard|list
        """
        cards = card.PaymentCard.__subclasses__()
        matchs = []

        for card_type in cards:
            try:
                new_card_instance = card_type(numbers)
                matchs.append(new_card_instance)
            except IllegalPaymentCardNumbers:
                pass

        return matchs.pop() if len(matchs) == 1 else matchs

