"""
6. Find­ing Re­main­der With­out Us­ing
'%' Op­er­a­tor
Write a method re­main­der which takes two in­te­ger ar­gu­ments, div­i­dend and di­visor, and re­turns the re­main­der when div­i­dend is di­vid­ed by di­vi­sor. Do NOT use
the mod­u­lus op­er­a­tor (%) to cal­cu­late the re­main­der!
As­sump­tion

Div­i­dend will al­ways be greater than or equal to di­vi­sor.

Notes
Make sure that the im­ple­ment­ed re­main­der func­tion works ex­act­ly the same as the
Mod­u­lus op­er­a­tor (%).

"""

def reminder(dividend,divisor):
   return dividend - divisor * (dividend//divisor)
    
if __name__ == '__main__':
    print(reminder(10,7))