def vypocet(asirky_pocet = None):
    protihrac:str; sirky_pocet:int; uzivatel_volba:int; prepocet:int; vzorec:int
    
    sirky_pocet = int(input("Zadej počet sirek pro zahájení hry: ")) 
    print(f"Pocet sirek je: {sirky_pocet}")
    protihrac = input("Zadej jméno protiháče: ") 

    while sirky_pocet > 0:
        try:
            uzivatel_volba = int(input("Jsi na řade. Zadej počet, kt. chceš odebrat: ")) 
        except:
            print("Špatné číslo nebo symbol. Zadejte prosím číslo '1', '2' nebo '3'.\n")
        
        sirky_pocet-= uzivatel_volba
        print(f"Zbylý počet sirek: {sirky_pocet}")
    
        if sirky_pocet == 0:
            print("\nZvítezil jsi! Blahopřeji.")
            break
 
        if sirky_pocet %4 == 0:
            vzorec = 1
        else:
            prepocet = sirky_pocet - int(sirky_pocet/4) # musim vzdy odecitat pocet, kolik preskocim 4,8,12,...
            vzorec = (prepocet+2)%3+1 # int nahore, je kuli zaohrouhleni na cele cislo, protze delim
        """
        if sirky_pocet == 1: vzorec = sirky_pocet - 1
        if sirky_pocet == 2: vzorec = sirky_pocet - 2
        if sirky_pocet == 3: vzorec = sirky_pocet - 3    
        if sirky_pocet == 4: vzorec = sirky_pocet - 1
        if sirky_pocet == 5: vzorec = sirky_pocet - 1
        if sirky_pocet == 6: vzorec = sirky_pocet - 2
        if sirky_pocet == 7: vzorec = sirky_pocet - 3
        if sirky_pocet == 8: vzorec = sirky_pocet - 1
        if sirky_pocet == 9: vzorec = sirky_pocet - 1
        if sirky_pocet == 10: vzorec = sirky_pocet - 2
        if sirky_pocet == 11: vzorec = sirky_pocet - 3
        if sirky_pocet == 12: vzorec = sirky_pocet - 1
        if sirky_pocet == 13: vzorec = sirky_pocet - 1
        if sirky_pocet == 14: vzorec = sirky_pocet - 2
        if sirky_pocet == 15: vzorec = sirky_pocet - 3
        """
        # posloupnost je 1,2,3,1,1,2,3,1,1,2,3,1,... -> vyberu 1,2,3 posl. a nasl. 1 je vzdy po 4.kroce
        # urcim si n-tej clen 1,2,3,1,2,3,... -> nejdriv najdu mod3 -> prictu 1 a nakonec posunu i o 2
     
        sirky_pocet-= vzorec
        print(f"Na tahu je {protihrac}. Zůstalo {sirky_pocet} sirek.\n")
    
        if sirky_pocet == 0: print(f"Bohužel, zvítezil '{protihrac}'!")

def hra_sirky():        
    titulek= "VÍTEJ VE HŘE 'SIRKY'!\n---------------------\n"
    titulek+= "Tvým úkolem je odebírat sirky z kopy po jedné, dvou, a nebo tří."
    titulek+= "\nCílem je odebrat všechny sirky jako první.\n"
    print(titulek)
    vypocet()
    
hra_sirky()

