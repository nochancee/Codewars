number = 1
guess = int(input('Enter an Integer:'))
guess1 = abs(guess - number)
holodno = list(range(21,40))
teplo = list(range(11,20))
goryacho = list(range(6,10))
very_goryacho = list(range(1,5))

if guess == number:
    print('Congratulations, you guessed it.')
elif guess1 >= 50:
    print('Очень холодно')
elif guess1 in holodno:
    print('Холодно')
elif guess1 in teplo:
    print('Тепло')
elif guess1 in goryacho:
    print('Горячо')
elif guess1 in very_goryacho:
    print('Очень горячо')

    