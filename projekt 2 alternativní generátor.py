ss
from random import choice
def generator_cisel():
    cisla_do_deviti = []
    for číslo in range(0,10):
        cisla_do_deviti.append(číslo)
    cislo1 = choice(cisla_do_deviti[1:])
    cisla_do_deviti.remove(cislo1)
    cislo2 = choice(cisla_do_deviti)
    cisla_do_deviti.remove(cislo2)
    cislo3 = choice(cisla_do_deviti)
    cisla_do_deviti.remove(cislo3)
    cislo4 = choice(cisla_do_deviti)
    
    tajenka = str(cislo1) + str(cislo2) + str(cislo3) + str(cislo4)
    print(tajenka)


generator_cisel()  





        




        

    

    






        

    
            
    