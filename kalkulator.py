#inportowanie 
import math

#1Podanie liczb i działania 
print('Liczba 1 jest pierwsa z koleji więc: od niej zostanie coś odjęte, ona zostanie podzielona, i ona zostanie pomnożona przez liczbę 2')
znak = input('Podaj znak działania: ')
#liczba 1
a= float(input('Podaj liczbę 1: '))
#liczba 2
b = float(input('Podaj liczbę 2: '))

#2Sprawdzenie błędów 
if znak == '/' and a or b == 0 :
    print('Nie dzielimy przez 0')
    print(znak, a, b)
    exit()

#3Dalsze działania na liczbach 

if znak == '+' :
    print('wynik to:',a + b)

elif znak == '-':
    print('wynik to:',a - b)

elif znak == '*':
    print('wynik to:',a * b)

elif znak == '/' and a or b != 0: 
    print('wynik to:',a / b)

elif znak == '^':
    print('potengi jeszcze nie działają')

elif znak == '~':
    print('pierwiastkowanie jeszcze nie działa ')
    
    

##Sprawdzenie działanie punktu 1 
print(znak, a, b)
