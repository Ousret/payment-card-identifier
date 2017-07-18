from payment_card_identifier.card import PaymentCard, IllegalPaymentCardNumbers


class CardIdentifier:

    @staticmethod
    def from_numbers(numbers):
        """
        Try to identify and create instance of card.
        :param str numbers: Card numbers
        :return: An VISA, MasterCard, Amex, etc.. instance, List of match or None.
        :rtype: PaymentCard|list|None
        """
        cards = PaymentCard.__subclasses__()
        matchs = []

        for card_type in cards:
            try:
                new_card_instance = card_type(numbers)
                matchs.append(new_card_instance)
            except IllegalPaymentCardNumbers:
                pass

        nb_match = len(matchs)

        return matchs.pop() if nb_match == 1 else matchs if nb_match > 1 else None
