"""
3. Sum of 2 largest integers
    Create a function that returns the sum of the two highest positive numbers given an array of
    minimum 4 positive integers. No floats or non-positive integers will be passed.
    For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 119.

"""

def sum_largest(num):
    if num[0] > num[1]:
        large_1, large_2 = num[0], num[1]
    else:
        large_1, large_2 = num[1], num[0]

    for i in range(2, len(num)):
        if num[i] >= large_2:
            if num[i] >= large_1:
                large_2 = large_1
                num[i], large_1 = large_1, num[i]
            else:
                large_2, num[i] = num[i], large_2

    return (large_1 + large_2)


if __name__ == '__main__':
    print(sum_largest([19, 5, 42, 2, 77]))
    print(sum_largest([10, 343445353, 3453445, 3453545353453]))