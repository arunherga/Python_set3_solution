"""
7) Length of longest word in list
Complete the function that takes one argument, a list of words, and returns the length of the
longest word in the list.
For example:
['simple', 'is', 'better', 'than', 'complex'] ==> 7
Do not modify the input list.

"""

def longest_word(str):
  long = 0
  for i in str:
    if len(i) > long:
      long = len(i)
  return long

if __name__ == '__main__':
  print(longest_word(['simple', 'is', 'better', 'than', 'complexity']))