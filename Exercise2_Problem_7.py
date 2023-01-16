"""
7. Remove String Spaces
    Simple, remove the spaces from the string, then return the resultant string.
    $this->assertSame('8j8mBliB8gimjB8B8jlB', no_space('8 j 8 mBliB8g imjB8B8 jl B'));
    $this->assertSame('88Bifk8hB8BB8BBBB888chl8BhBfd', no_space('8 8 Bi fk8h B 8 BB8B B
    B B888 c hl8 BhB fd'));
    $this->assertSame('8aaaaaddddr', no_space('8aaaaa dddd r '));

"""

def no_space(text):
    t = text.replace(' ','')
    return t

if __name__ == '__main__':
    print(no_space("8 j 8 mBliB8g imjB8B8 jl B"))
    print(no_space('8 8 Bi fk8h B 8 BB8B B B B888 c hl8 BhB fd'))
    print(no_space('8aaaaa dddd r '))

