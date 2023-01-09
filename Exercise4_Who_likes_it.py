"""
1) 1. Who likes it?
You prob­a­bly know the "like" sys­tem from Face­book and oth­er pages. Peo­ple can
"like" blog posts, pic­tures or oth­er items. We want to cre­ate the text that should be
dis­played next to such an item.
Im­ple­ment the func­tion which takes an ar­ray con­tain­ing the names of peo­ple
that like an item. 
It must re­turn the dis­play text as shown in the ex­am­ples:
[] --> "no one likes this"
["Peter"] --> "Peter likes this"
["Jacob", "Alex"] --> "Jacob and Alex like this"
["Max", "John", "Mark"] --> "Max, John and Mark like
this"
["Alex", "Jacob", "Mark", "Max"] --> "Alex, Jacob and 2 others
like this"
Note: For 4 or more names, the num­ber in "and 2 oth­ers" sim­ply in­creas­es.

"""
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

if __name__ == '__main__':
  print(likes(['arun']))
  print(likes(['arun','ram']))
  print(likes(['arun','ram','sam']))
  print(likes(['arun','ram','sam','bam','jam']))