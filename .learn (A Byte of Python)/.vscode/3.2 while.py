number = 0
running = True
holodno = list(range(21, 41))
teplo = list(range(11, 21))
goryacho = list(range(6, 11))
very_goryacho = list(range(0, 6))
while running:
    guess = int(input('Enter an Integer:'))
    guess1 = abs(guess - number)
    if guess == 0:
        guess1 = 0
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess1 >= 41:
        print('Очень холодно')
    elif guess1 in holodno:
        print('Холодно')
    elif guess1 in teplo:
        print('Тепло')
    elif guess1 in goryacho:
        print('Горячо')
    elif guess1 in very_goryacho:
        print('Очень горячо')
        
else:
    print('Цикл while закончен.')

print('Завершение.')