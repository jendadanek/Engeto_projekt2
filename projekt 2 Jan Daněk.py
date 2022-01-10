from random import choice
ss
def main():
    tajenka = str(choice(generator_cisel()))
    cows = 0
    bulls = 0
    while True:
        hadani= input("Zadej svůj typ na číslo od 1000 do 9999: ")
        mnozina_hadani = set()
        for symbol in hadani:
            mnozina_hadani.add(symbol)

        kontrola_inputu(hadani, mnozina_hadani, tajenka, cows, bulls)


def kontrola_inputu(hadani, mnozina_hadani, tajenka, cows, bulls):
    if hadani.isnumeric() == False:
        print("Neplatné číslo.")
        
    elif len(hadani) != 4:
        print("Špatně délka čísla.")
        
    elif int(hadani) not in range(1000,9999):
        print("číslo nesmí začínat nulou.")
           
    elif len(mnozina_hadani) != 4:
        print("Čísla se v zadaném čísle nemůžou opakovat.")
    
    else: pocitani(hadani, tajenka, cows, bulls)

def pocitani(hadani, tajenka, cows, bulls):
    for index, číslo in enumerate(hadani):
            if číslo in tajenka and  číslo != tajenka[index]:
                cows += 1
            elif číslo == tajenka[index]:
                bulls += 1
    
    vypis(bulls, cows)        


def vypis(bulls, cows):
    if bulls == 1 and cows == 1:
        print("bull:",bulls, "cow:", cows)
                                   
    elif bulls == 4:
        print("vyhrál jsi")
        quit()
    elif bulls == 1 and cows != 1:
        print("bull:",bulls, "cows:", cows)
                    
    elif bulls != 1 and cows == 1:
        print("bulls:",bulls, "cow:", cows)
                  
    elif bulls != 1 and cows != 1:
        print("bulls:",bulls, "cows:", cows)


def generator_cisel():
    mnozina = set()
    seznam_tajenka = []
    for číslo in range(1000,10000):
        for hodnota in str(číslo):
            mnozina.add(hodnota)
        if len(mnozina) ==4:
            seznam_tajenka.append(číslo)    
        mnozina = set()
    return seznam_tajenka
        
main()



    

            
    


