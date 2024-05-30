warehouse_status=int; warehouse_limit:int; laod:int; unload:int; state:float; option:str
warehouse_status = 100
warehouse_limit = 1000

def ware_load():
    global warehouse_status
    while True:
        try:
            load = int(input("Kolik kusů chcete naskladnit? -> "))
            break
        except ValueError:
            print("Chyba! Opakujte volbu.")
    if load > warehouse_limit-warehouse_status: 
        print("Zboží nelze naskladnit. Zkontroluj kapacitu skladu.")
    elif load <= 0:
        print("Chybný počet kusů! Opakujte volbu.") 
    else: 
        warehouse_status+= load
        print("Zboží bylo naskladněno.")

def ware_unload():
    global warehouse_status
    try:
        unload = int(input("Kolik kusů chcete vyskladnit? -> "))
    except ValueError:
            print("Chyba! Opakujte volbu.")
    if warehouse_status < unload: 
        print("Zboží nelze vyskladnit. Zkontroluj kapacitu skladu.")
    elif unload <= 0:
        print("Chybný počet kusů! Opakujte volbu.") 
    else: 
        warehouse_status-= unload
        print("Zboží bylo vyskladněno.")

def check():
    state = (warehouse_status/warehouse_limit)*100
    print(f"Ve skladu je aktuálně {warehouse_status} ks zboží. Sklad zaplněn ze {round(state,2)} %. Máme místo pro {warehouse_limit-warehouse_status} ks.")

def warehouse_control():
    while True:
        print("\n---------------SKLAD---------------")
        print("Pro naskladnení tovaru zadejte: '+'")
        print("Pro vyskladnení tovaru zadejte: '-'")
        print("Pro kontolu tovaru zadejte: 'c'")
        print("Pro ukončení apliakce zadejte: 'end'")
        print("...................................")
        option = input("Vaše volba -> ")
        if option == "+": ware_load()
        elif option == "-": ware_unload()
        elif option == "c": check()
        elif option == "end": exit()
        else:
            print("Chyba! Opakujte volbu.")
    
warehouse_control()





    

