"""
4. Number of People in the Bus
    There is a bus moving in the city, and it takes and drops some people in each bus stop.
    You are provided with a list (or array) of integer pairs. Elements of each pair represent the
    number of people getting into the bus (The first item) and the number of people who get off the
    bus (The second item) in a bus stop.
    Your task is to return the number of people who are still in the bus after the last bus station (after
    the last array). Even though it is the last bus stop, the bus is not empty and some people are still
    in the bus, and they are probably sleeping there :D

    Take a look at the test cases.
    Please keep in mind that the test cases ensure that the number of people in the bus is always
    >= 0. So the return integer can't be negative.
    The second value in the first integer array is 0, since the bus is empty in the first bus stop.
    [[10,0],[3,5],[5,8]] => 5
    [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]] => 17
    [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]] => 21

"""

def number_in_bus(num):
    people_left = 0

    for i, j in enumerate(num):
        people_left += (j[0] - j[1])
    
    return people_left


if __name__ == '__main__':
    print(number_in_bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))
    print(number_in_bus([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
    print(number_in_bus([[10,0],[3,5],[5,8]]))