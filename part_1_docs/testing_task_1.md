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


  def check_for_ace(self, card):
    if card.value = 1: # single equal sign '=' should be a double equal sign '=='
      return True
    else   # missing ':'
      return False
   

  dif highest_card(self, card1 card2): #'dif' should be 'def', missing a comma ',' after 'card1'
  if card1.value > card2.value: # the whole line starting from 'if' should be indented
    return card #'card' isnt defined, it should be 'card1'
  else: #should have the same indentation as the if statement on line 28
    return card2
  


def cards_total(self, cards) #this line should be indented, also missing a colon ':' at the end
  total #total needs to be defined or assigned a value like 'total = 0'
  for card in cards: #should be indented
    total += card.value
    return "You have a total of" + total # it should read: return f"You have a total of {total}"

  
