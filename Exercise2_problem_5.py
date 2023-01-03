"""
5. Invert values
    Given a set of numbers, return the additive inverse of each. Each positive becomes negatives,
    and the negatives become positives.
    invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
    invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
    invert([]) == []
    You can assume that all values are integers. Do not mutate the input array/list.

"""

def invert_values(num):
    for i in range(len(num)):
        num[i] *= -1
    
    return num


if __name__ == '__main__':
    print(invert_values([1,2,3,4,5]))
    print(invert_values([1,-2,3,-4,5]))
    print(invert_values([1,-2,3,-4,5]))
    print(invert_values([]))