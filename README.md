payment-card-identifier
-----------------------

Payment card identifier provides a useful utility method for determining a credit card type from both fully qualified and partial numbers.
Same as braintree/credit-card-type but in Python.

#### How to

```python
from payment_card_identifier import CardIdentifier

my_card = CardIdentifier.from_numbers('4532040524589053')

print(my_card)
print(my_card.json)
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