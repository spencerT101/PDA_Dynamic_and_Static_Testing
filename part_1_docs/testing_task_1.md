### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# Incorrect syntax in IF statement. It should be 'card.value == 1:'
#Incorrect syntax for ELSE statement, needs a semi colon.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False


# The function is spelt incorrectly. It shoulde be 'DEF' not 'DIF;
# There is a comma missing between the CARD1 and CARD2 parameters in the function.   
# The IF RETURN statement should be card1.

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total is undefined should be set to 'total = 0'
# total needs to be converted into string in return statement.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
