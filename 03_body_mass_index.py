line:str; text:str; result:bool; height=float; weight=float; denom:float; index:float; option:str
line = "-----------------------------------"

def intro():
    global result
    text = f"Vítejte v aplikaci pro výpočet BMI.\n{line}\nZadejte vaši výšku v centimetrech a váhu v kilogramech."
    print(text)
    result = True

def load_height():
    global height
    try:
        height = float(input("Výška [cm]: "))
    except ValueError:
        text = "Nesprávná hodnota. Zadejte číslo!"
        print(text)
        load_height()

def load_weight():
    global weight
    try:
        weight = float(input("Váha [kg]: "))
    except ValueError:
        text = "Nesprávná hodnota. Zadejte číslo!"
        print(text)
        load_weight()
        
def check():
    global result
    if  weight <=10 or weight >= 635 or height <= 70 or height >= 272: # Jon Brower Minnoch (weight record) and Robert Wadlow (height record)
        result = False
        return result
     
def process():
    global text
    if result:
        denom = (height/100)**2
        index = weight/denom
        if index <= 15: category = "velmi vážnu podvýživu"
        elif 15 < index <= 16: category = "vážnu podvýživu"
        elif 16 < index <= 18.5: category = "podvýživu"
        elif 18.5 < index <= 25: category = "normální hodnoty"
        elif 25 < index <= 30: category = "nadváhu"
        elif 30 < index <= 35: category = "nadváhu I. stupňe"
        elif 35 < index <= 40: category = "nadváhu II. stupňe"
        elif 40 < index: category = "nadváhu III. stupňe"
        text = f"Váš BMI je roven hodnotě {round(index,2)}. Máte {category}."
        return text
    else:
        text = "Některý vámi zadaný parametr neodpovídá parametrům člověka. Výpočet nelze realizovat."
        return text
      
def output():
    print(text, "\nPřejete si opakovat výpočet? ")
    while True:
        option = input("Zvolte: a/n -> ")
        if option == "n":
            print(f"Děkuji za použití BMI softvéru.\n{line}")
            exit()
        elif option == "a":
            print(f"{line}\n")
            bmi()
            break
        else:
            print("CHYBA! Opakujte volbu prosím.")

def bmi():    
    intro()
    load_height()
    load_weight()
    check()
    process()
    output()
    
bmi()
