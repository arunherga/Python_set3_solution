"""
3)Re­place with al­pha­bet po­si­tion
Wel­come.
In this kata you are re­quired to, giv­en a string, re­place every let­ter with its po­sition in the al­pha­bet.
If any­thing in the text isn't a let­ter, ig­nore it and don't re­turn it.
"a" = 1, "b" = 2, etc.

Ex­am­ple

alphabet_position("The sunset sets at twelve o' clock.")

Should re­turn ”20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12
22 5 15 3 12 15 3 11" ( as a string )

"""

def alphabet_position(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  text = text.lower()
  result = []
  for char in text:
    if char in alphabet:
      result.append(str(alphabet.index(char)+1))
  return ' '.join(result)

if __name__ == '__main__':
  print(alphabet_position("The sunset sets at twelve o' clock."))
