from payment_card_identifier.constant import *
import re
import json


class IllegalPaymentCardNumbers(Exception):
    pass


class LuhnChecksumDoesNotMatchException(IllegalPaymentCardNumbers):
    pass


class PaymentCard:

    def __init__(self, name, regex, numbers):
        """
        :param str name: 'Brand name' or type of the card.
        :param str regex: Used regex to verify numbers
        :param str numbers: Fully qualified card numbers
        """

        self._name = name
        self._regex = re.compile(regex)
        self._numbers = numbers

        if not self.is_valid:
            raise IllegalPaymentCardNumbers('"{0}" are not valid numbers for {1} card type.'.format(self._numbers, self._name))
        if not PaymentCard.luhn_verify(self._numbers):
            raise LuhnChecksumDoesNotMatchException('"{0}" does not pass luhn mod-10 checksum for {1} card type.'.format(self._numbers, self._name))

    @property
    def name(self):
        return self._name

    @property
    def regex(self):
        return self._regex

    @property
    def numbers(self):
        return self._numbers

    def masked_numbers(self, masked_char='X'):
        """
        Display masked numbers, only show 4 last digits.
        :param str masked_char: Used char to replace
        :return: Masked numbers expect 4 last digits
        :rtype: str
        """
        return (masked_char * (len(self.numbers) - 4)) + self.numbers[-4:]

    @property
    def is_valid(self):
        return self._regex.fullmatch(self._numbers) is not None

    @staticmethod
    def luhn_verify(numbers):
        """
        Custom verification for card numbers.
        :param str numbers: Fully qualified card numbers
        :return: True if passed, False otherwise.
        :rtype: bool
        """
        v_sum = 0
        num_digits = len(numbers)
        oddeven = num_digits & 1

        for count in range(0, num_digits):
            digit = int(numbers[count])

            if not ((count & 1) ^ oddeven):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9

            v_sum += digit

        return (v_sum % 10) == 0

    @property
    def json(self):
        return json.dumps(self, default=lambda o: o.__dict__ if not isinstance(o, re._pattern_type) else o.pattern,
                          sort_keys=True, indent=4)


class VISA(PaymentCard):

    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, VISA_CARD_RE, numbers)


class MasterCard(PaymentCard):

    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, MASTER_CARD_RE, numbers)


class Amex(PaymentCard):

    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, AMEX_CARD_RE, numbers)


class BCGLOBAL(PaymentCard):

    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, BCGLOBAL_CARD_RE, numbers)


class CarteBlanche(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, CARTE_BLANCHE_CARD_RE, numbers)


class DinersClub(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, DINERS_CLUB_CARD_RE, numbers)


class Discover(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, DISCOVER_CARD_RE, numbers)


class InstaPayment(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, INSTA_PAYMENT_CARD_RE, numbers)


class JCB(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, JCB_CARD_RE, numbers)


class KoreanLocal(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, KOREAN_LOCAL_CARD_RE, numbers)


class Laser(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, LASER_CARD_RE, numbers)


class Maestro(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, MAESTRO_CARD_RE, numbers)


class Solo(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, SOLO_CARD_RE, numbers)


class Switch(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, SWITCH_CARD_RE, numbers)


class UnionPay(PaymentCard):
    def __init__(self, numbers):
        super().__init__(self.__class__.__name__, UNION_PAY_CARD_RE, numbers)

