protihrac:str; sirky_pocet:int; uzivatel_volba:int; prepocet:int; vzorec:int; text:str

def uvitej():
    text= "VÍTEJ VE HŘE 'SIRKY'!\n---------------------\n"
    text+= "Tvým úkolem je odebírat sirky z kopy po jedné, dvou, a nebo tří."
    text+= "\nCílem je odebrat všechny sirky jako první.\n"
    return print(text)

def nactiData():
     global sirky_pocet, protihrac
     protihrac = input("Zadej jméno protiháče: ")
     while True:
        try:
            sirky_pocet = int(input("Zadej počet sirek pro zahájení hry: ")) 
            if sirky_pocet < 3 or sirky_pocet > 500:
                print("Zadejte prosím počet v rozmezí od 3 do 500.") 
                continue
            else:
                print(f"Pocet sirek je: {sirky_pocet}")
                break
        except ValueError:
            print("Chyba při zadávaní, zadejte číslo prosím znova.") 

def vypocet(): 
    global sirky_pocet
    text = "Špatné číslo nebo symbol. Zadejte prosím číslo '1', '2' nebo '3'.\n"
    while sirky_pocet > 0:
        while True:
            try:
                uzivatel_volba = int(input("Jsi na řade. Zadej počet, kt. chceš odebrat: "))
                if uzivatel_volba >= 4 or uzivatel_volba <= 0:
                    print(text)
                    continue
                else:
                    break
            except:
                print(text)
        
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
    uvitej()
    nactiData()
    vypocet()
    
hra_sirky()

