bulb_works:bool; power_on:bool

print("Kontrola žárovky.") 
bulb_works = input("Žárovka svítí? (a/n) -> ") == "a" # -> je 0 nebo 1
if bulb_works: pass 
else:
    power_on = input("Je napájena? (a/n) -> ") == "a"
    if power_on: print("Vyměnit žárovku.")
    else:
        print("Zapnout napájení.")
        bulb_works = input("Žárovka svítí? (a/n) -> ") == "a"
        if bulb_works: pass
        else: print("Vymenit žárovku.")
print("Hotovo!")
            