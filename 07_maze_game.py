# bludiste z mistnosti
# kazda mistnost ma 4 sousedy (S-V-J-Z), kt. nemusi byt dosazitelni
# zakladny prvek je bunka

class CBunka: # datova trida repre 1 bunku
    ss = int(); vs = int(); js = int(); zs = int() # kdyz se tam neda jit, je tam none, kdyz jo tak tam je cislo souseda, ss - severni soused
    def __init__(self, ass, avs, ajs, azs): 
        self.ss = ass
        self.vs = avs
        self.js = ajs
        self.zs = azs
    
class CBunky:
    bunky = list()
    def pridej(self, ass, avs, ajs, azs):
        self.bunky.append(CBunka(ass,avs,ajs,azs))

    def demo(self): 
        # bunka = CBunka(None,2,None,None); bludiste.bunky.append(bunka) #bunku musim pridat do bludite
        self.pridej(None, 1, None, None) # bunka s čislom 0, jediny mozny pohyb vs z 0 do 1
        self.pridej(None, None, 4, 0)
        self.pridej(None, None, 5, None)
        self.pridej(None, 4, 6, None)
        self.pridej(1, 5, None, 3)
        self.pridej(2, None, 8, 4)
        self.pridej(3, 7, None, None)
        self.pridej(None, None, None, 6)
        self.pridej(5, None, None, None)

class CHra: 
    aktual = 0 
    cil = 6 
    bludiste = CBunky() 
    bludiste.demo()
    
    def __init__(self): # tento konstruktor je hlavny program
        while True:
            volba = input(f"({self.aktual}) Zvolte smer (s,v,j,z nebo k = konec).") 
            if volba == "k": break
            elif volba in {"s","v","j","z"}: self.krok(volba)
            else: print("Nerozumim pozadavku :-/.")
    def krok(self,asmer): # ak dostane smer tak co ma urobit
        #self.bludiste.bunky[self.aktual].vypis()
        oaktual = self.bludiste.bunky[self.aktual] 
        if asmer == "s" and oaktual.ss != None: self.aktual = oaktual.ss # neni tam none = neni tam stena, aktualna bunka sa aktualizuje na suseda
        elif asmer == "v" and oaktual.vs != None: self.aktual = oaktual.vs
        elif asmer == "j" and oaktual.js != None: self.aktual = oaktual.js
        elif asmer == "z" and oaktual.zs != None: self.aktual = oaktual.zs
        else: print("Tudy cesta nevede!")
        if self.aktual == self.cil: 
            print("Jste v cili :). Díky za hru!")
            exit()
        
hra=CHra()

  
    

