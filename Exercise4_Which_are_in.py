"""
4) Which are in
Giv­en two ar­rays of strings a1 and a2 re­turn a sort­ed ar­ray r in lex­i­co­graph­i­cal order of the strings of a1 which are sub­strings of strings of a2.
Ex­am­ple 1:
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]
3
Ex­am­ple 2:
a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []

"""

def in_array(a1, a2):
  res = []
  for s1 in a1:
    for s2 in a2:
      if s1 in s2:
        if s1 not in res:
          res.append(s1)
  return sorted(res)

if __name__ == '__main__':
  a1 = ["arp", "live", "strong"]
  a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
  print(in_array(a1,a2))