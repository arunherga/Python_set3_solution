"""
5. Iso­gram
An iso­gram is a word that has no re­peat­ing let­ters, con­sec­u­tive or non-con­sec­u­tive.
Im­ple­ment a func­tion that de­ter­mines whether a string that con­tains only let­ters is
an iso­gram. As­sume the emp­ty string is an iso­gram. Igno­re let­ter case.
Ex­am­ple: (In­put --> Out­put)
"Der­mato­glyph­ics" --> true "aba" --> false "moOse" --> false (ig­nore let­ter
case)

"""

def is_isogram(string):
  string = string.lower()
  char = set()
  for character in string:
    if character in char:
      return False
    else:
      char.add(character)
  return True



if __name__ == '__main__':
  print(is_isogram('Dermatoglyphics'))
  print(is_isogram('aba'))
  print(is_isogram('moOse'))
  
