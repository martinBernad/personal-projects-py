nr1:float; nr2:float; oper:str; repeat:str; result:float; status:bool

def intro():
    global result, status
    print("Kalkulačka vás vítá!")
    print("Zadejte dvě čísla a pak operátor k příslušné matematické operaci.", "\n-----------------------------------------------------------------")
    result = 0 
    status = True
    
def load():
    global nr1, nr2
    while True:
        try:
            nr1 = float(input("Zadejte 1. číslo: "))
            if status:
                break
            else:
                continue
        except ValueError:
            print("CHYBA! Zadejte znovu.")
    while True:
        try:    
            nr2 = float(input("Zadejte 2. číslo: "))
            if status:
                break
            else:
                continue
        except ValueError:
            print("CHYBA! Zadejte znovu.")
    
def operator():
    global oper
    oper = input("Zadejte operátor (+,-,*,/): ")

def process():
    global result, oper
    if oper == "+": result = nr1 + nr2
    elif oper == "-": result = nr1 - nr2 
    elif oper == "*": result = nr1 * nr2
    elif oper == "/": 
        try:
            result = nr1 / nr2
        except ZeroDivisionError:
            print("Nulou nelze delit!")
            status = False
    else:
        print("CHYBA! - chybný operátor") # check input of load()
        status = False
        operator()
        process()

def display():
    if status: 
        print(f"{nr1} {oper} {nr2} = {round(result,4)}")

def escape():
    repeat = input("Chcete znova použít kalkulačku? (a/n): ")
    if repeat == "a":
        print() 
        kalkulacka()
    elif repeat == "n": 
        print("Nashledanou.")
        exit()
    else: 
        print("CHYBA! Opakujte volbu prosím: ")
        escape()

def kalkulacka(): 
    intro() 
    load()
    operator()
    process()
    display()
    escape()
    
kalkulacka() # code initialization
