"""
2. Sum of 2 smallest integers
    Create a function that returns the sum of the two lowest positive numbers given an array of
    minimum 4 positive integers. No floats or non-positive integers will be passed.
    For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
    [10, 343445353, 3453445, 3453545353453] should return 3453455.

"""

def sum_smallest(num):

    if num[0] < num[1]:
        small_1, small_2 = num[0], num[1]
    else:
        small_1, small_2 = num[1], num[0]

    for i in range(2, len(num)):
        if num[i] <= small_2:
            if num[i] <= small_1:
                small_2 = small_1
                num[i], small_1 = small_1, num[i]
            else:
                small_2, num[i] = num[i], small_2

    return (small_1 + small_2)


if __name__ == '__main__':
    print(sum_smallest([10, 343445353, 3453445, 3453545353453]))
    print(sum_smallest([19, 5, 42, 2, 77]))
