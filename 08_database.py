class CZamec:
    idzam = int() 
    prijmeni = str()
    jmeno = str()
    plat = int()
    
    def __init__(self, aidzam):  # kdyz vznikne zamestanec -> priradim mu id
        self.idzam = aidzam 
    def vypis(self):
        print(self.idzam, self.prijmeni, self.jmeno, self.plat)

class CZamci:
    seznam = list()
    idpristi = 1 # nesouvisi s indexem, cislovani zamestance od 1
    def zapis0(self, aprijmeni, ajmeno, aplat, aidzam=None): 
        if aidzam == None:
            zamec = CZamec(self.idpristi); self.idpristi+=1 
        else:
            zamec = CZamec(aidzam)
        zamec.prijmeni = aprijmeni; zamec.jmeno = ajmeno; zamec.plat = aplat 
        self.seznam.append(zamec) 

    def demo(self):
        print("\nPRIDANI UKAZKOVYCH ZAZNAMU")
        self.zapis0("Novák","Jozef",50000) 
        self.zapis0("Novákova","Jozefa",60000)
        self.zapis0("Petrus","Karel",30000)
        self.zapis0("Veselá","Jana",22000)
        self.zapis0("Chytrý","Dominik",150000)
        self.vypis()  

    def zapis(self):
        print("\nZADANI NOVEHO ZAMESTANCE.")
        prijmeni = input("Prijmeni: ") 
        jmeno = input("Jmeno: ")
        plat = int(input("Plat: "))
        self.zapis0(prijmeni, jmeno, plat)

    def hledej(self):
        print("\nHLEDANI ZAMESTNANCE")
        cast_prijmeni = input("Zadejte alepoň část příjmení: ")
        for zamec in self.seznam:
            if cast_prijmeni.lower() in zamec.prijmeni.lower(): zamec.vypis() 

    def edituj(self):
        self.hledej()
        print("\nEDITACE ZAMESTANCE")
        idzam = int(input("Zadejte Id zamestance, kt. chcete editovat: ")) 
        zamec = self.seznam[self.IdNaIndex(idzam)] 
        zamec.vypis() 
        if input("Prijmeni - ENTER další položka, 'e' pro editaci: ") == "e":
            zamec.prijmeni = input("Prijmeni: ")
        if input("Jmeno - ENTER další položka, 'e' pro editaci: ") == "e":
            zamec.jmeno = input("Jmeno: ")
        if input("Plat - ENTER další položka, 'e' pro editaci: ") == "e":
            zamec.plat = int(input("Plat: "))
        
    def IdNaIndex(self,aidzam): 
        index = 0
        for zamec in self.seznam:
            if zamec.idzam == aidzam: break
            index+=1
        return index
    
    def smaz0(self, aidzam): 
        self.seznam.pop(self.IdNaIndex(aidzam))

    def smaz(self):
        self.hledej()
        print("\nSMAZANI ZAMESTNANCE") 
        self.smaz0(int(input("Zadejte Id zamestance, ktereho chcete smazat: ")))

    def vypis(self):
        print("\nVYPIS ZAMESTNANCU") 
        for zamec in self.seznam: zamec.vypis()

    def uloz0(self, ajmeno_souboru, aoddelovac):
        fp = open(ajmeno_souboru, "w", encoding="utf-8") 
        for zamec in self.seznam:
            fp.write(str(zamec.idzam)+aoddelovac) # zamec je objektova lokalni promenna, idzam je vlastnost
            fp.write(zamec.prijmeni+aoddelovac)
            fp.write(zamec.jmeno+aoddelovac)
            fp.write(str(zamec.plat)+"\n") 
        fp.close()

    def uloz(self): 
        print("\nULOZENI ZAMESTANCU DO CSV")
        oddelovac = input("Zvolte oddelovac dat (; nebo ,): ")
        jmeno_souboru = input("Zadejte jmeno souboru bez pripony: ")+".csv"
        self.uloz0(jmeno_souboru,oddelovac) 

    def vycisti(self): # kdyz chci nacitat data tak musim predesle data co tam jsou zmazat -> protoze se budou mixovat indexy
       self.seznam.clear() # zrusi seznam, ale iba vnutro (destroy zmaze aj list)

    def nacti0(self, ajmeno_souboru, aoddelovac):
        self.vycisti() # zrusi objekty v seznamu
        with open(ajmeno_souboru, "r", encoding="utf-8") as fp: 
            seznam0=pf.readines() 
        idmax = 0
        for zamec0 in seznam0: 
            bunky = zamec0.split(aoddelovac) 
            idzam = int(bunky[0])
            if idzam > idmax:
                idmax = idzam
            self.zapis0(bunky[1],bunky[2],int(bunky[3]),idzam) # nechcem index
            self.idpristi = idmax+1         

    def nacti(self):
        print("\nNACTENI CSV DO SOUBORU")
        jmeno_souboru = input("Zadejte jmeno souboru bez pripony: ")+".csv"
        oddelovac = input("Zvolte oddelovac dat (; nebo ,): ")
        self.nacti0(jmeno_souboru,oddelovac)
    
class CRizeni: 
    zamci = CZamci() 
    def __init__(self):
        while True:
            print("------------------------------")
            print("d - demo")
            print("z - zapiš")
            print("h - hledej")
            print("e - edituj")
            print("s - smaž")
            print("u - ulož")
            print("n - načti")
            print("v - vypiš")
            print("k - konec")
            volba = input("Vaše volba: ").lower()
            if volba == "k": break
            elif volba == "d": self.zamci.demo() 
            elif volba == "z": self.zamci.zapis()
            elif volba == "h": self.zamci.hledej()
            elif volba == "e": self.zamci.edituj()
            elif volba == "s": self.zamci.smaz()
            elif volba == "v": self.zamci.vypis()
            elif volba == "u": self.zamci.uloz()
            elif volba == "n": self.zamci.nacti()
            else: print("Chybná volba.")
        print("Nashledanou.")
        
riznei = CRizeni()      
    