"""
9. Coding 3min : Reading a Book
    John was reading a book. When he sees a word that he has never read, he will read the word
    spelling, each letter(not for punctuation,number, only letter) takes 1 second; If he has read the
    word, he will read the word, each word takes 1 second.

    Give you a parameter words(Each word is separated by space)
    Return a number that shows how many seconds John can finish reading.
    Example:
    sc("Hello World!")=10
    John read all the word spelling.
    sc("black cat and white cat all are cat")=24
    John read the 2nd 'cat' and 3rd 'cat' used 2 seconds.
    sc("black Cat and white cat all are cat")=24
    'Cat' and 'cat' are same words,your code should ignore the case
    words1="Related Articles: Ruby Environment, CoffeeScript Environment, JavaScript
    Environment, Python Environment, Haskell Environment, Java Environment, Clojure
    Environment, .NET Environment."
    sc(words1)=86
    words2="Related Articles: Ruby Environment, Coffee Script Environment, Java Script
    Environment, Python Environment, Haskell Environment, Java Environment, Clojure
    Environment, .NET Environment."
    sc(words2)=78
    CoffeeScript is one word, Coffee Script are two words

"""

def reading_time(article):
    text = list(article.split(" "))
    text_1 = []
    for word in text:
        result = ""
        for i in word:
            if i.isalpha():
                result = ''.join([result,i])
        text_1.append(result)
    
    time = 0
    check = []
    for word in text_1:
        if word in check:
            time += 1
        else:
            time += len(word)
            check.append(word)
    return time


if __name__ == '__main__':
    print(reading_time('Hello World!'))
    print(reading_time('black cat and white cat all are cat'))
    print(reading_time('Related Articles: Ruby Environment, CoffeeScript Environment, JavaScript Environment, Python Environment, Haskell Environment, Java Environment, Clojure Environment, .NET Environment.'))
    print(reading_time('Related Articles: Ruby Environment, Coffee Script Environment, Java Script Environment, Python Environment, Haskell Environment, Java Environment, Clojure Environment, .NET Environment.'))

