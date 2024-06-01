import random
import datetime
import os
sourad:str(); souradnce:dict(); sourad_x:tuple(); sourad_y:tuple(); zivot:int()
sourad_y = (1,2,3,4,5,6,7,8,9,10)
sourad_x = ("A","B","C","D","E","F","G","H","I","J")
zivot = 10; n = 10 # pocet zivotu ve hre a pocet radku pole
pozice = ["  A B C D E F G H I J"]

def vypis_souradnice(): # udelam slovnik a priradim kazdemu znaku poradove cislo (dulezite pro propojeni)
    global souradnice # aby exist. pristup v propoj
    souradnice = dict()
    for klic in sourad_x:
        ind = sourad_x.index(klic) # udela z klice cislo od 0
        souradnice[klic] = ind+1 # nechci cisla od 0, chci A->1, B->2, ...  
    
class CPole:
    ax=int(); ay=int(); n=int(); symbol = str()
    print()
    pozice# moznost dynamizovat -> zvetsit v zavislosti na "n"
    def vypis(n,ax=1,ay=1,asymbol="X"):
        global prazdne_pole
        for i in range(1,n): # naplneni pole radkami
            fp=open("proj_lode_prazdnePole.txt", "a", encoding = "utf-8")
            if i == 1: print(pozice[0]) # titulek pole A B C D E ...
            if ay == i:
                radek_str = f"{i} ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"
                dil = radek_str.split()
                dil[ax] = asymbol
                radek_str = spoj(dil)
            else:
                radek_str = f"{i} ~ ~ ~ ~ ~ ~ ~ ~ ~ ~"
            # if i > 9: radek_str = f"{i} ~ ~ ~ ~ X ~ ~ ~ ~ ~" posun pro vic nez n=10, cislo 10 ma 2 cislice -> vznika posun v konzole!
            fp.write(f"{radek_str}\n")
            fp.close()
            print(radek_str) # vypsani pole do konzole
            with open("proj_lode_prazdnePole.txt", "r", encoding = "utf-8") as fp:
                prazdne_pole = fp.read()

def spoj(astr): # dodelat s pomoci + a vyhodit join()
    string = " "
    return string.join(astr)

def tah_uzivatel(): # kontrola vstupu uzivatele ()
    global sourad, sourad1, sourad2, zivot # aby je slo pouzit v propoj
    sourad = input("Zadej dvojici palebních souřadnic: ")
    
    try:
        sourad1 = sourad[0]; sourad2 = sourad[1]
    except:
        IndexError: print("Nespravne zadani, opakuj.")
    if len(sourad) == 2: # uzivatel zadal dvojici čislo a znak
        try:
            sourad1 = int(sourad1) # nevim co to je, input vraci str -> otestuju, zda ho lze prevest -> ano: je to cislo, ne je to znak
            if sourad1 in sourad_y:
                try:
                    sourad2 = int(sourad2)
                    h1.hl_chyba()
                    tah_uzivatel()
                except:
                    if sourad2.upper() in sourad_x:
                        print() #print("OK") ## ladeni - pak zmazat ##
                    else:
                        h1.hl_chyba()
                        tah_uzivatel()
            else:
                h1.hl_chyba()
                tah_uzivatel()
        except:
            if sourad1.upper() in sourad_x: # uzivatel zadal prvni znak, chce zadat dvojici znak a cislo
                try:
                    sourad2 = int(sourad2)
                    if sourad2 in sourad_y:
                        print() #print("OK") ## ladeni - - pak zmazat ##
                    else:
                        h1.hl_chyba()
                        tah_uzivatel()
                except:
                    h1.hl_chyba()
                    tah_uzivatel()
            else:
                h1.hl_chyba()
                tah_uzivatel()
    elif sourad.lower() == "radar":
        radar()
        tah_uzivatel()
    elif sourad.lower() == "restart":
        volba_restart = input("Opravdu cheš restartovat? (a/n): ")
        print()
        while volba_restart != "a" and volba_restart != "n":
            volba_restart
        if volba_restart == "a":
            print("------------------------")
            hra()
        if volba_restart == "n":
            print(".............jdeme dál............")
            tah_uzivatel()
    elif sourad.lower() == "zivot":
        zivot+= 1
        print("Dorazili posily!", f"Obranné pozice byli navýšeny: {zivot}\n")
        tah_uzivatel()
    elif sourad.lower() == "konec": exit()
    else:
        h1.hl_chyba()
        tah_uzivatel()

def propoj():  # uzivatel zadal "XY" -> propojeni znaku a cisel s realnou pozicii v poli
    global sourad1, sourad2, ind1, ind2
    try:
        sourad1 = int(sourad1) # zkoumam, zda-li zadal prvni cislo nebo znak (zada napr. 3D, by default chci D3)
        ind2 = sourad1
        ind1 = souradnice[sourad2.upper()] # zadal prvni cislo a pak pro druhou vybere ze slovnika souradnice prislusny index k pismenu
    except: # souradn1 neni cislo -> zadal znak (pro prehlednost zavedu ind1 a ind2 a taky pro zmenu, zada-li uzivatel 3D misto D3)
        ind1 = souradnice[sourad1.upper()] # vyberu jeho index pomoci slovnika
        ind2 = sourad2 # sourad2 je osetrena, je to cislo a je to urcite int
 
def pc_pozice(): # vymyslet aby nemali tie iste pozicie
    global y1, x1, y2, x2, y3, x3, y4, x4, y5, x5
    ind1:int(); ind2:int()

    y1 = int(random.random()*n)
    x1 = random.randint(1,n-1) # index x pre cislo a y pre pismeno, cis 1 je lod 1
    
    y2 = random.randint(1,n-1) 
    x2 = random.randint(1,n-1) 
    
    y3 = random.randint(1,n-1)
    x3 = random.randint(1,n-1)
    
    y4 = random.randint(1,n-1)
    x4 = random.randint(1,n-1)
    
def radar():
    print(f"\nNeznámý objekt 'A1->(?,1)': (?,{x1}),(?,{x2}),(?,{x3}),(?,{x4})\n") 
        
def vymen(ax,ay): # logika zmen
    for i in range (1,n):
        if ay == 1: return ax
        if ay == i+1: return ax+i*11
 
def tah():
    global zivot, y1, x1, y2, x2, y3, x3, y4, x4, sourad, sourad1, sourad2
    
    tah_uzivatel()# tah uzivatele
    if sourad == "konec":
        print("opravdu končíme? (a/n)")
        ukonceni = input("Vaše odpověď: ")
        while ukonceni != "a" and ukonceni != "n":
            if ukonceni == "a":
                sourad1 = 1
                sourad2 = "A"
                zivot = 0
            elif ukonceni == "n":
                tah()
            else:
                print("Chyba! Zadej znova.")
                ukonceni = input("Vaše odpověď: ")
        
    vypis_souradnice() # slouzi k rpopojeni (seznam)
    propoj()
    if volba_ur == "l": cis = urovne.lehka()
    if volba_ur == "s": cis = urovne.stredni()
    if volba_ur == "t": cis = urovne.tezka(zivot)
    
    if y1 == ind1 and x1 == ind2:
        casti[vymen(y1,x1)] = "X"
        x1 = 0 # zabezpecim, ze v dalsim behu uz nebude podminka nikdy splnena -> plavidlo jiz potopeno
        h1.hl_zasah()
    elif y2 == ind1 and x2 == ind2:
        casti[vymen(y2,x2)] = "X"
        x2 = 0 
        h1.hl_zasah()
    elif y3 == ind1 and x3 == ind2:
        casti[vymen(y3,x3)] = "X"
        x3 = 0 
        h1.hl_zasah()
    elif (y4 == ind1 and x4 == ind2):
        casti[vymen(y4,x4)] = "X"
        x4 = 0 
        h1.hl_zasah()
    else:
        casti[vymen(ind1,ind2)] = "."
        zivot-= cis
        h1.hl_voda()

    # vymena souradnice
    text = spoj(casti) # spojovani spatky do textu
    
    text1 = text[:22]
    text2 = text[22:44]
    text3 = text[44:66]
    text4 = text[66:88]
    text5 = text[88:110]
    text6 = text[110:132]
    text7 = text[132:154]
    text8 = text[154:176]
    text9 = text[176:]
    
    print(pozice[0])
    print(text1 +"\n"+text2+"\n"+text3+"\n"+text4+"\n"+text5+"\n"+text6+"\n"+text7+"\n"+text8+"\n"+text9)
    print()
  
def log():
    global jmeno
    jmeno = str()
    aktual_cas = datetime.datetime.now()
    cas = aktual_cas.strftime("%H:%M:%S")
    datum = aktual_cas.strftime("%d.%m.%Y")
    jmeno = input("Zadejte jméno hráče: ")
    zaznam = f"Hra byla spuštena hráčem {jmeno}: {datum};{cas}\n" 

    with open("log_lode.txt", "a", encoding = "utf-8") as fp:
        fp.write(zaznam)

class CHlasky:
    seznam = list(); nah = int();
    def hl_chyba():##(self):
        seznam = ["-- Špatné souřadnice! Opakuj volbu. --\n", "-- Soustřed se! Zkus to znova. --\n", "-- Chyba! Tudy cesta nevede. --\n"]
        seznam.append("-- Neznámá kombinace. Zadejte palebné pozice! --\n")
        nah = random.randint(0,len(seznam)-1)
        print(seznam[nah])
    
    def hl_voda():
        smer = ["doleva", "doprava"]
        seznam = [f"-- Voda! {random.randint(2,15)}° {smer[random.randint(0,1)]}. --\n", "-- Opět voda kapitáne. Miřte lépe! --\n", "-- Voda! Palte znova a lépe! --\n"]
        seznam.append("-- Zasa Voda. Kapitáne, my ty granáty nekrademe! --\n")
        nah = random.randint(0,len(seznam)-1)
        print(seznam[nah])
    
    def hl_zasah():
        seznam = ["-- Zásah! Paráda! --\n", "-- Zásah! Skvěle kapitáne, jen tak dál. --\n", "-- Exploze! Plnej zásah. --\n"]
        seznam.append("-- Zásah! Jdou ke dnu. --\n")
        nah = random.randint(0,len(seznam)-1)
        print(seznam[nah])
    
    def hl_vitez():
        seznam = ["Nepřítel byl zničen!\nPřístav je volný.", "Nepřítel je poražen!\nBlokáda je u konce."]
        seznam.append("Bitva je u konce, blahopřeji kapitáne. Zvítezili sme.\n")
        nah = random.randint(0,len(seznam)-1)
        print(seznam[nah])
        
    def hl_prohra():
        seznam = ["Nedá se nic dělat.\nNepřítel prolomil všechny naše pozice.", "Už nemáme žádnou munici!\nMusíme kapitulovat."]
        seznam.append("Kapitáne! Všechna naše palebná postavení byla zničena.\n")
        nah = random.randint(0,len(seznam)-1)
        print(seznam[nah])

def start():
    global volba_menu
    print("~~ HRA VÁLEČNÉ LODĚ ~~\n")
    popisek = "Cílem hry Válečné lodě je zničit všechny lodě nepřítele. Palba je zahájena dvojicí souřadnic"
    popisek+= " typu celé číslo a znak (nebo obráceně). Například 'A6'. V palbě se střídáte s počítačem, "
    popisek+= "který respektuje vámi zvolenou volbu obtížnosti. Ve hře existuje taky náhoda a nepřítel se nemusí vždy trefit."
    popisek+= " Pokud se tak stane, zníží se vaše obranné body (život) - 'Zbývající obranné pozice'. Zničíte-li všechny lodě, zvítězili jste."
    popisek+= " Jestli se váš život zníží na nulu a nepovede se vám potopit lodě, prohrajete. Když zasáhnete, pálite znova bez ztáty životů"
    popisek+= ". Když se netrafíte, může zasáhnout nepřítel. Doprovodné hlášky a lodě nepřítele jsou náhodne generovány na začátku každé nové hry."
    print(popisek,"\n")
    log()
    print("\n================================================================================================")
    text = f"Vítej v Líbii {jmeno}. Píše se konec roku 1941 a tvá vojska čelí nepříteli z vody, vzduchu i země.\n"
    text+= "Tvým úkolem je otevřít zásobovací tepnu u města Tobruk a prolomit ponorkovou blokádu přístavu.\n\nHodně štěstí kapitáne,"
    text+= " tvůj čas je omezen!"
    print(text)
    while True:
        volba_menu = input("\nDále do menu (m) nebo ukonči(k): ").lower()
        if volba_menu == "k":
            print("\nNashledanou.")
            break
        if volba_menu == "m":
            menu()
            break
        else: print("Chybná volba.")  

def konec():
    if os.path.exists("proj_lode_prazdnePole.txt"):
        os.remove("proj_lode_prazdnePole.txt")

def menu():
    print()
    while True:
        print("     VÍTEJ HERNÍM V MENU:\n------------------------------")
        print("(z) - zahájit novou hru")
        print("(k) - ukončit hru")
        print("\n~~~~~~~ ZADÁVEJ VE HŘE ~~~~~~~")
        print("(restart) - restartuje hru")
        print("(zivot) - přidá 1 život")
        print("(radar) - provede průzkum")
        print("(konec) - ukončuje hru\n------------------------------")
        volba_menu = input("Zadejte vaši volbu: ").lower()
        if volba_menu == "z":
            hra()
            break # opousti, aby po ukonceni hry nepustil znova menu
        elif volba_menu == "k":
            print("Nashledanou.")
            break # -//-
        else: print("\nChybná volba.\n")
        
def uroven():
    global volba_ur
    print("  Zvolte obtížnost\n-------------------\n lehká: (l)\n střední: (s)\n těžká: (t)\n-------------------")
    volba_ur = input("Vaše volba úrovně: ").lower()
    while volba_ur != "l" and volba_ur != "s" and volba_ur != "t":
        print("Špatná volba, opakujte prosím.")
        volba_ur = input("Vaše volba úrovně: ")
               
class CUrovne:
    def lehka():
        return random.randint(0,1)
    def stredni():
        return random.randint(0,2)
    def tezka(acis):
        vysl = random.randint(0,int(acis/2))
        if zivot == 1:
            vysl = 1
        return vysl

def hra():
    global zivot #<- global, aby sa zmnil 0 na novy
    print()
    zivot = 10 ### <- potreba nacitat novy zivot!!
    uroven()
    prubeh()
    opakovat_hru()

def opakovat_hru(): # tu niekde je chyba, a -> spusti sa volba urovne -> po volbe sa cykli a opyta zas ci chce hrat znova
        volba_konec = input("\nChceš si zahrát znova? (a/n): ").lower()
        while volba_konec != "a" and volba_konec != "n":
            print("Nerozumím poždavku. Zkus to znova.")
            volba_konec  
        if volba_konec == "a":
            print("-------------------------------")
            print()
            hra()
        if volba_konec == "n":
            print("~~ Hra byla ukončena ~~")
    
def prubeh(): 
    global casti
    print()
    konec()
    pole.vypis(n,1,1,"~") 
    pc_pozice() # rozmistni svoje lode
    casti = prazdne_pole.split() # uz tady (ne uvnitr tah())
    ### zivot sa po nacitani novej hry ak sa opakuje nenacita znova, ostane = 0 -> preto hra konci ihned!, musi tu byt znova
    while zivot>0:
        print(f"Zbývající obranné pozice: {zivot}")
        tah() # obecny tah uzivatele - jeno kolo
        if x1 == 0 and x2 == 0 and x3 == 0 and x4 == 0:
            h1.hl_vitez()
            print("--KONEC HRY--")
            break
        if zivot == 0:
            h1.hl_prohra()
            print(f"\nPozice nepřítele: ({y1},{x1}), ({y2},{x2}), ({y3},{x3}), ({y4},{x4})")
            print("--KONEC HRY--")
            break

h1 = CHlasky 
urovne = CUrovne
pole = CPole

start()




    




