"""
2. String ends with
Com­plete the so­lu­tion so that it re­turns true if the first ar­gu­ment(string) passed in
ends with the 2nd ar­gu­ment (also a string).
Ex­am­ples:
solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false

"""

def string_end(str,ending):
  return str[-len(ending):] == ending

if __name__ == '__main__':
  print(string_end('abc', 'bc'))
  print(string_end('abc', 'd'))