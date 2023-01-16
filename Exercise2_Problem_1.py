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
    while number > 0:
        n = number % 10
        reverse_list.append(n)
        number = int(number/10)
    return reverse_list



if __name__ == '__main__':
    print(number_reverse_list(3452))  
    print(number_reverse_list(0))


