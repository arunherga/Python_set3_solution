"""
10. Are You Playing Banjo?
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!
    The function takes a name as its only argument, and returns one of the following strings:
    name + " plays banjo"
    name + " does not play banjo"
    Names given are always valid strings.
    assert.strictEqual(areYouPlayingBanjo("Adam"), "Adam does not play banjo");
    assert.strictEqual(areYouPlayingBanjo("Paul"), "Paul does not play banjo");
    assert.strictEqual(areYouPlayingBanjo("Ringo"), "Ringo plays banjo");
    assert.strictEqual(areYouPlayingBanjo("bravo"), "bravo does not play banjo");
    assert.strictEqual(areYouPlayingBanjo("rolf"), "rolf plays banjo");

"""

def areYouPlayingBanjo(name):
    n = name.lower()
    n = list(n)
    if n[0] == 'r':
        return ("%s plays banjo" %name)
    else:
        return ("%s does not play banjo" % name)

if __name__ == '__main__':
    print(areYouPlayingBanjo("Adam"))
    print(areYouPlayingBanjo("Paul"))
    print(areYouPlayingBanjo("Ringo"))
    print(areYouPlayingBanjo("bravo"))
    print(areYouPlayingBanjo("rolf"))