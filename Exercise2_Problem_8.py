"""
8. Shortest Word
    Given a string of words, return the length of the shortest word(s).
    String will never be empty and you do not need to account for different data types.
    $this->assertSame(3, findShort("bitcoin take over the world maybe who knows perhaps"));
    $this->assertSame(3, findShort("turns out random test cases are easier than writing out
    basic ones"));
    $this->assertSame(3, findShort("lets talk about javascript the best language"));
    $this->assertSame(1, findShort("i want to travel the world writing code one day"));
    $this->assertSame(2, findShort("Lets all go on holiday somewhere very cold"));
    $this->assertSame(2, findShort("Let's travel abroad shall we"));

"""

def find_short(text):
    text_1 = list(text.split(" "))
    smallest = len(text_1[0])

    for i in text_1:
        if len(i) <= smallest:
            smallest = len(i)
    
    return smallest


if __name__ == '__main__':
    print(find_short("bitcoin take over the world maybe who knows perhaps"))
    print(find_short("turns out random test cases are easier than writing out basic ones"))
    print(find_short("lets talk about javascript the best language"))
    print(find_short("i want to travel the world writing code one day"))
    print(find_short("Lets all go on holiday somewhere very cold"))
    print(find_short("Let's travel abroad shall we"))