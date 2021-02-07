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
# constructor missing, add: 
#def __init__(self):
    #self.cards = []

  def check_for_ace(self, card):
    if card.value = 1:
    #'=' is for assignment, it needs to be '==' to check it is equal
      return True
    else
    # else needs a colon, i.e 'else:'
      return False
   

  dif highest_card(self, card1 card2):
  #typo, 'dif' should be 'def' and a comma between card1 and card2 in the arguments
  if card1.value > card2.value:
#indentation error, this if statement should be indented by two spaces/1 tab. 
    return card
    #error, this should return 'card1', not 'card'.
  else:
    return card2
  


def cards_total(self, cards):
#indentation error, needs to be indented
  total
  #indentation error, needs to be indented
  #total needs to be set to 0, i.e. 'total = 0'
  #empty list added required in constructor named cards, and add method to add card to cards is required. 
  for card in cards:
    total += card.value
    return "You have a total of" + total
    #total is an integer. this needs formatting, i.e. it should return 'You have a total of {}'.format(total)
  
```
