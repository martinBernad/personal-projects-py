temps:list; option:str; option:str; new_temp:float; temps_fahrenheit:float; temps_kelvin:float
err = "\nERR! Bad input. Repeat your option."
temps = []; temps_fahrenheit = []; temps_kelvin = [] 

def temp_load():
    global temps
    option = "y"
    while option == "y":
        option = input("Do you want to add temperature? (y/n) -> ")
        if option == "y": 
            while True:
                try:
                    new_temp = float(input("Enter new measurement temperatue: "))
                    temps.append(new_temp)
                    break
                except ValueError:
                    print(err)
        elif option == "n":
            print(f"\nMeasured temperatures are {temps} °.")
            break
        else:
            option = "y"
            print(err)

def temp_sort():
    while True:
        option = input("What do you want to sort? Celsius, Kevin or Fahrenheit? (c,k,f) -> ")
        if option == "c":
            temperature = temps
            break
        elif option == "k": 
            temperature = temps_kelvin
            if temperature == []:        
                print("\nFiles are missing! Start with temp. conversation.\n")
                convert()
            else: break
        elif option == "f": 
            temperature = temps_fahrenheit
            if temperature == []:        
                print("\nFiles are missing! Start with temp. conversation.\n")
                convert()
            else: break    
        else: print(err)
    while True:
        option = input("For ascending type 'a', for descending type 'd' -> ")
        if option == "a": 
            temperature.sort()
            print(f"\nSorted! {temperature}.")
            break
        elif option == "d": 
            temperature.sort(reverse=True)
            print(f"\nSorted! {temperature}.")
            break
        else: print(err)
    
def temp_max():
    t_max = float('-inf')
    for temp in temps:
        if temp > t_max: t_max = temp
    print(f"\nThe maximal temperature is {t_max}°.")

def temp_min():
    t_min = float('inf')
    for temp in temps:
        if temp < t_min: t_min = temp
    print(f"\nThe minimal temperature is {t_min}°.")

def convert():
    global temps_kelvin, temps_fahrenheit
    while True:
        print("Convert degree Celsius to Fahrenheit -> 'cf'")
        print("Convert degree Celsius to Kelvin -> 'ck'")
        option = input("Choose conversion -> ")
        if option == "cf": 
            if temps_fahrenheit == []:
                for temp in temps:
                    temp_fahrenheit = (temp * 1.8) + 32
                    temps_fahrenheit.append(round(temp_fahrenheit,2))
                print(f"\nConverted! {temps} ° -> {temps_fahrenheit} F.\n")
                break
            else: 
                print("\nFiles has been convereted yet.")
                break
        elif option == "ck":
            if temps_kelvin == []:
                for temp in temps:
                    temp_kelvin = temp + 273.15
                    temps_kelvin.append(round(temp_kelvin,2))
                print(f"\nCoverted! {temps} ° -> {temps_kelvin} K.\n")
                break
            else:
                print("\nFiles has been convereted yet.")
                break
        else: print(err)

def menu():
    while True:
        print("\n---------------MENU----------------")
        print("For maximumu enter: 'max'")
        print("For maximumu enter: 'min'")
        print("For sorting enter: 's'")
        print("For temp. conversation enter: 'c'")
        print("Show all temperatures: 'a'")
        print("For exit enter: 'end'")
        print("-----------------------------------")
        option = input("Enter your option -> ")
        if option == "max": temp_max()
        elif option == "min": temp_min()
        elif option == "s": temp_sort()
        elif option == "c": convert()
        elif option == "a": print(f"\n{temps} °",f"{temps_kelvin} K",f"{temps_fahrenheit} F", sep='\n')
        elif option == "end": 
            print("Thank you for using this software.\n")
            break
        else: print(err)

def control(): 
    temp_load()
    menu()

print("\nWelcome to thermometer app.")
control()