payment-card-identifier [![Build Status](https://travis-ci.org/Ousret/payment-card-identifier.svg?branch=master)](https://travis-ci.org/Ousret/payment-card-identifier) [![codecov](https://codecov.io/gh/Ousret/payment-card-identifier/branch/master/graph/badge.svg)](https://codecov.io/gh/Ousret/payment-card-identifier)
-----------------------

Payment card identifier provides a useful utility method for determining a credit card type from both fully qualified numbers.
Same as braintree/credit-card-type but in Python.

#### How to

```python
from payment_card_identifier import CardIdentifier

my_card = CardIdentifier.from_numbers('4532040524589053')

print(my_card)
# <payment_card_identifier.card.VISA object at 0x10b336b38>
print(my_card.json)
# {
#    "_name": "VISA",
#    "_numbers": "4532040524589053",
#    "_regex": "^4[0-9]{12}(?:[0-9]{3})?$"
# }
```

#### Currently supported cards

- VISA
- MasterCard
- Amex
- BCGLOBAL
- CarteBlanche
- DinersClub
- Discover
- InstaPayment
- JCB
- KoreanLocal
- Laser
- Maestro
- Solo
- Switch
- UnionPay


#### WiP

This is still work in progress project.
Currently under dev.

*Todo list:*

- Create .from_partials(numbers)