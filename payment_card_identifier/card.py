from payment_card_identifier.constant import *
import re


class IllegalPaymentCardNumbers(Exception):
    pass


class PaymentCard:

    def __init__(self, name, regex, numbers):
        """
        :param str name:
        :param str regex:
        :param str numbers:
        """

        self._name = name
        self._regex = re.compile(regex)
        self._numbers = numbers

        if not self.is_valid:
            raise IllegalPaymentCardNumbers('"{0}" are not valid numbers for {1} card type.'.format(self._numbers, self._name))

    @property
    def name(self):
        return self._name

    @property
    def regex(self):
        return self._regex

    @property
    def is_valid(self):
        return self._regex.fullmatch(self._numbers) is not None

    def c_verify(self):
        """
        Custom verification for card numbers.
        :return: True if passed, False otherwise.
        :rtype: bool
        """
        return NotImplemented


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

