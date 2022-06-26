def get_count(sentence):
    number_of_vowels = 0
    if sentence == '':
        return(0)
    for d in sentence:
        if d == 'a' or d == 'e' or d == 'i' or d == 'o' or d == 'u':
            number_of_vowels += 1
        elif d == 'y':
            number_of_vowels += 0
    print(number_of_vowels)
    return(number_of_vowels)


get_count("ardz otgirq xaxbai asbokzmilj tehak lcxzoloamr aga gsewoi kxmnopfreis xnyea")

def getCount(s):
    return sum(c in 'aeiou' for c in s)