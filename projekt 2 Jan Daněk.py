from random import choice

def main():
    tajenka = str(choice(generator_cisel()))
    cows = 0
    bulls = 0
    while True:
        hádání = input("Zadej svůj typ na číslo od 1000 do 9999: ")
        množina_hádání = set()
        for symbol in hádání:
            množina_hádání.add(symbol)
        kontrola_inputu(hádání, množina_hádání, tajenka, cows, bulls)


def kontrola_inputu(hádání, množina_hádání, tajenka, cows, bulls):
    if hádání.isnumeric() == False:
        print("Neplatné číslo")
        

    elif len(hádání) != 4:
        print("špatně délka čísla")
        

    elif int(hádání) not in range(1000,9999):
        print("číslo nesmí začínat nulou")
        
        
    elif len(množina_hádání) != 4:
        print("Čísla se v zadaném čísle nemůžou opakovat")
    
    else: počítání(hádání, tajenka, cows, bulls)

def počítání(hádání, tajenka, cows, bulls):
    for index, číslo in enumerate(hádání):
            if číslo in tajenka and  číslo != tajenka[index]:
                cows += 1
            elif číslo == tajenka[index]:
                bulls += 1
    výpis(bulls, cows)        


def výpis(bulls, cows):
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
    množina = set()
    seznam_tajenka = []
    for číslo in range(1000,10000):
        for hodnota in str(číslo):
            množina.add(hodnota)
        if len(množina) ==4:
            seznam_tajenka.append(číslo)    
        množina = set()
    return seznam_tajenka
        

main()



    

            
    


