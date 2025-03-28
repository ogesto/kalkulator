#inportowanie 
import math

#1Podanie liczb i działania 
print('Liczba 1 jest pierwsa z koleji więc: od niej zostanie coś odjęte, ona zostanie podzielona, i ona zostanie pomnożona przez liczbę 2')

#znak
znak = input('Podaj znak działania: ')

#liczba 1
a= float(input('Podaj liczbę 1: '))

#liczba 2
b = float(input('Podaj liczbę 2: '))

#Dalsze działania na liczbach 

if znak == '+' :
    print('wynik to:',a + b)

elif znak == '-':
    print('wynik to:',a - b)

elif znak == '*':
    print('wynik to:',a * b)

elif znak == '/':
    if  b == 0: 
        print('Nie dzielimy przez 0')
        print(a,znak, b)
        exit()
    else:
        print('wynik to:',a / b)

elif znak == '^':
    odp = a ** b
    print('wynik to:',odp)

elif znak == '!':
    odp = a ** (1/b)
    print('wynik to:', odp)
    

#Sprawdzenie działanie punktu 1 
print(znak, a, b)

print('koniec')

exit()
