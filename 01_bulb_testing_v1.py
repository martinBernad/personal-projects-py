option:str; err:str; change:str

def test():
    err = "CHYBA!"
    change = "Musíte vyměnit žárovku."
    option = input("Svítí žárovka? (a/n)\n")
    if option == "a":
        pass
    elif option == "n":
        option = input("Je žárovka připojena na zdroj el. energie? (a/n)\n")
        if option == "a":
            print(change)
            pass
        elif option == "n":
            print("Připojite zdroj el. energie!")
            option = input("Svítí žárovka? (a/n)\n")
            if option == "a":
                pass
            elif option == "n":
                print(change)
                pass
            else:
                print(err)
        else:
            print(err)
    else:
        print(err)          

def bulb():
        print("Zkontrolujte žárovku.")
        test()
        print("Ďekuji za kontrolu.")
        
bulb()

