#inportowanie 
import math

#Podanie liczb i działania 
print('Liczba 1 jest pierwsa z koleji więc: od niej zostanie coś odjęte, ona zostanie podzielona, i ona zostanie pomnożona przez liczbę 2')

#znak
znak = input('Podaj znak działania: ')

#liczba 1
a = float(input('Podaj liczbę 1: '))

#liczba 2
b = float(input('Podaj liczbę 2: '))

#Dalsze działania na liczbach 

#dodawanie
if znak == '+' :
    print('wynik to:',a + b)

#odejmowanie 
elif znak == '-':
    print('wynik to:',a - b)

#mnożenie
elif znak == '*':
    print('wynik to:',a * b)

#dzielenie
elif znak == '/': 
    #Sprawdzenie błędów 
    if b == 0 :
        print('Nie dzielimy przez 0')
        print(znak, a, b)
        exit()  
    else:
        print('wynik to:',a / b)

#potęgowanie
elif znak == '^':
    print('wynik to:',a ** b)

#pierwiastkowanie 
elif znak == '!':
    print('wynik to:',a ** (1/b))  

    
##Sprawdzenie przypisywania 
print(a, znak, b)

print('koniec')
