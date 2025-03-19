#inportowanie 
import math

def calc(num1, num2, znak): #Funkcja która oblicza wynik działań
    if znak == "+": # Jeżeli znak to "+" wtedy
        return num1 + num2
    elif znak == "-":# Jeżeli znak to "-" wtedy
        return num1 - num2
    elif znak == "*":# Jeżeli znak to "*" wtedy
        return num1 * num2
    elif znak == "/":# Jeżeli znak to "/" wtedy
        if num1 == 0 or num2 == 0: #Jeżeli a lub b to 0 wtedy zwracamy błąd dzielenia przez zero
            return ZeroDivisionError
        return num1 / num2
    elif znak == "^":# Jeżeli znak to "^" wtedy
        return num1 ** num2
    elif znak == "~":# Jeżeli znak to "~" wtedy
        return math.sqrt(num1, num2) # Używamy wbudowanej funkcji która weżmie pierwiastek num2 stopnia z num1
        

def main(): # Funkcja główna w której jest cały kod
    #1Podanie liczb i działania 
    print('Liczba 1 jest pierwsa z koleji więc: od niej zostanie coś odjęte, ona zostanie podzielona, i ona zostanie pomnożona przez liczbę 2')
    znak = input('Podaj znak działania: ')
    #liczba 1
    a= float(input('Podaj liczbę 1: '))
    #liczba 2
    b = float(input('Podaj liczbę 2: '))

    print(f"{a}{znak}{b} = {calc(a, b, znak)}") #Zwrócenie wyniku w ładnej formie

main() # Wywołanie funkcji main()