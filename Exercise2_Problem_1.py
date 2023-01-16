"""
1. Convert a number into a reversed array of digits
    Given a random non-negative number, you have to return the digits of this number within an
    array in reverse order.
    Ex:
    0 => [0]
    3452 => [2,5,4,3]

"""

def number_reverse_list(number):
    reverse_list = []
    
    for i,j in enumerate(str(number)):
        reverse_list.append(int(j))

    return reverse_list[::-1]


if __name__ == '__main__':
    print(number_reverse_list(3452))  
    print(number_reverse_list(0))


