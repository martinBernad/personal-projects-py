import sys
from datetime import date
import datetime
from math import pi
import math
import calendar

"""
# SPECIFIC OUTPUT
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are\n")

# Information of module (library).
import math
import os
print(dir(math))
help(math) # details of module

# PY VERSON 
print("PYthon version:")
print(sys.version)
print("Version info")
print(f"{sys.version_info}\n")

# CURRENT DATE/TIME
now = datetime.datetime.now()
print("Current date & time:",now.strftime("%Y-%m-%d %H:%M:%S")); print()

# CIRCLE AREA
r = float(input("Insert radius of circe -> "))
area = pi*r*r
print(f"Area of circle with radius {r} is {round(area,2)}.\n")

# REVERSE NAME
name = input("Insert surname -> ")
lastName = input("Insert lastname -> ")
text = "Hi, " + lastName + " " + name + "!"
print(f"{text}\n")

# COMMA SEPARATED NRs
values = input("Insert comma separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple); print()

# FIND EXTENSION OF FILE
file_name = input("Insert name of the file: ")
file_list = file_name.split(".")
print("The extension of the file is : " + file_list[-1]); print()

# DISPLAY 1. AND LAST COLOR
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[-1]); print()

# extract the date from exam_st_date - use placeholders %
exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date); print()

# computes the value of n+nn+nnn, n=5 -> 615 (concatinate = spojovani retezce)
a = int(input("Input an integer: "))
n1 = int("%s" % a)          
n2 = int("%s%s" % (a, a))   
n3 = int("%s%s%s" % (a, a, a)) 
print(n1 + n2 + n3); print()

# Print the docstring (documentation) of the 'abs' function
print(abs.__doc__); print()

# calendar for a given month and year
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# CALCULATE NR. OF DAY BETWEEN (2014, 7, 2), (2014, 7, 11) - use "date from datetime"
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
delta = date2-date1
print(delta.days)

# difference between a given number and 17. If the number is greater than 17, return twice the absolute difference
def difference(n):
    if n <= 17: 
        return n-17
    else:
        return (n-17)*2
print(difference(25), difference(14))
print()

# calculate the sum of three given numbers. If the values are equal, return three times their sum
def sum(x,y,z):    
    sum = x+y+z
    if x == y == y == z:
        sum = 3*sum
        
    return sum
print(sum(3,5,8))
print(sum(2,2,2)), print()

# MAKE "n" COPYs OF TEXT "text"
def copy(text,n):
    result = ""
    for i in range(n):
        result = result + text
    return result
print(copy("Ahoj",1))
print(copy("Ahoj",5)), print()

# "n" IS EVEN OR ODD
num = int(input("Enter a number -> "))
mod = num % 2
if mod == 1: print("This is an odd number.\n")
else: print("This is an even number.\n")

# COUNT THE NUMBER 4 IN A GIVEN LIST
def counter(list:list):
    count = 0
    for i in range(len(list)):
        if 4 == list[i]:
            count+= 1
    return count
print(counter([1,4,8,1,4,41,8,4,5])); print()

# N COPPIES OF THE FIRST TWO CHARACTERS OF GIVEN STRING.
# RETURN N COPPIES OF THE STRING IF ITS LENGTH IS LESS THAN 2.
def stringCopy(n:int,text:str):
    if len(text) < 2: 
        return n*text
    else:
        return n*text[:2]
print(stringCopy(3,"cool")); print()

# TEST THE LETTER IF IS VOWL OR NOT
def testLetter(vowl:str):
    vowls = ["a","e","i","o","u"]
    if vowl in vowls: 
        result = f"'{vowl}' is Vowl."
    else: 
        result = f"'{vowl}' is not Vowl."
    return result
print(testLetter("a"))

def checkVowl(char:str):
    vowls = "aeiou"
    return char in vowls
print(checkVowl("f"))
print(checkVowl("e")); print()

# TEST IF THE VALUE IS INSIDE THE LIST
list1 = [1,2,4,5,"g"]
list2 = [",", 3, 3, 1, 8]
def checkValue(n:float, colection:list):
    for value in colection:
        if value == n:
            return True
    return False
print(checkValue(7,list1))

# CREATE HISTOGRAM FROM GIVEN LIST
def histogram(selection:list):
    for n in selection:
        print(n*"*")
histogram([2,4,2,1,5,2,9]); print()

# concentrate all elements in a list into a string and returns it
def concentrate(lst:list):
    result = ""
    for n in lst:
        result = result + str(n)
    return result
print(concentrate([13,3,4,2,6,7])); print()

# PRINT EVEN NRS IN THE SAME ORDER AND STOP AFTER 237
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
def selectNumbers(nrs:list):
    for n in nrs:
        if n == 237: break
        elif n%2 == 0: print(n)
selectNumbers(numbers); print()

# PRINT THE COLOR FROM 1 THAT IS NOT IN 2 -> output: {'Black', 'White'}
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
def selectColours(lst1:list, lst2:list):
    color_selection = list()
    for color in color_list_1:
        if color not in color_list_2:
            color_selection.append(color)
    return color_selection
print(selectColours(color_list_1, color_list_2))

print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2)); print()

# AREA OF TRIANGLE
def triangle_area(height:float, base:float):
    area = height*base/2
    return f"Area of the triangle with base {base} and height {height} is {area}."
print(triangle_area(4,5))

# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
def sum_function(x,y):
    sum = x + y
    if 15 < sum < 20:
        return 20
    else:
        return sum
print(sum_function(15,2))

# program to add two objects if both objects are integers
def add_numbers(a, b):
    # function that control if a and b are integers
    if not (isinstance(a,int) and isinstance(b,int)):
        return "Inputs are not integers!"
    else:
        return a+b
print(add_numbers(10, 20))   
print(add_numbers(10, 20.23)) 

# Write a Python program to solve (x + y) * (x + y)
def solve(x:float,y:float):
    result = (x + y) * (x + y)
    return result
print(solve(1,2))

# Write a Python program that displays your name, age, and address on three different lines
def getData(name:str, age:str, address:str):
    text = f"Name: {name}\nAge: {age}\nAddress: {address}"
    return text
print(getData("Martin", "32", "Suchy vrsek")) 

def personal_details():
    name, age, address = "Martin", 32, "Suchy vrsek"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
personal_details()

# Write a Python program to compute the future value of a specified principal amount (istina), rate of interest, and number of years.
def future_value():
    amount = float(input("Kolik je tvůj základ? (CZK): "))
    years = float(input("Na kolik let?: "))
    interest = float(input("Jaký je úrok? (např. 5%): "))
    value = amount*((1+(0.01*interest)))**years
    return value
print(f"Nová suma je {round(future_value(),2)}Kč.\n")

# Write a Python program to calculate the Euclidean distance between the points a = (x1, y1) and b = (x2, y2)
def distance(a:list,b:list):
    dist = math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)
    return dist
print(distance([4,0],[6,6]))

# Write a Python program to check whether a file "main.txt" exists -> True or False
import os.path
print(os.path.isfile("main.txt"))
print(os.path.isfile("README.md"))

# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# Use the 'calcsize' function to determine the size (in bytes) of the C int type for the current platform.
# The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size in bits.
import struct
print(struct.calcsize("P") * 8)

# Write a Python program to get information about your OS.
import platform
import os
import sysconfig
operating_system = platform.system() # 'Windows', 'Linux', or 'Darwin' (macOS)
name_os = os.name
version_os = platform.release() # 'posix', 'nt', 'java'
print("You are runing on {} with name '{}' and its version is {}.\n".format(operating_system, name_os, version_os))
print("os.name                     ", name_os)
print("sys.platform                ", sys.platform)
print("platform.system()           ", operating_system)
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())

# Write a Python program to get user name of PC.
import getpass
print(getpass.getuser())

# Write a Python program to locate Python site packages. (path for addons for py)
import site
print(site.getsitepackages())

# Write a Python program to find out the number of CPUs used.
import multiprocessing
cpu_count = multiprocessing.cpu_count() # the number of available CPU cores
print(cpu_count)

# Write a Python program to list all files in a directory.
from os import listdir
print(listdir(path= 'C:')) # return a list containing the names of the entries in the directory given by path

# Find absolute path of file.
import os
def abs_file_path(path_fname):
    return os.path.abspath(path_fname)
print("Absolute file path: ", abs_file_path("README.md"))

# Find the time of creation of file.
import os.path, time
create = time.ctime(os.path.getmtime("README.md"))
print("Last modified: %s" % create)



# A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
import cProfile
def sum():
   for i in range(1,100): print(i+i)
cProfile.run('sum()')

# Write a Python program to find local IP addresses of your computer using Python's stdlib.
import socket
local_hostname = socket.gethostname()
ip_list = socket.gethostbyname_ex(local_hostname)[2] # list of ip adresses that are reversed because of loopback teesting
print(ip_list[0])

# Measure the time of your program.
import time
def sum_of_n_numbers(n):
    start = time.time() # measurement starts
    s = 0 # initialize the sum to store the value
    for i in range(1, 1+n): 
        s = s + i
    end = time.time() # measurement ends
    return s, end - start
n = 50000
print(f"The sum of {n} numbers in a row is {sum_of_n_numbers(n)[0]} and required time to comupute is {sum_of_n_numbers(n)[1]}s.")

# Alteratives how to write a text using print().
height = 170.73
print("My height is:", height, "cm.")
print(f"This height is: {height} cm.")
print("Your height is: %d cm." %height) # d is for int and s is for str!
print("New height is: %.1f cm." %height)
print("The height is: {} cm.".format(height))

# Write a Python program to calculate sum of digits of a number.
def digits_sum(n):
    s = 0
    n = str(n)
    for i in range(0,len(n)):
        ni = n[i]
        s = s + int(ni)
    return s
n = 12345
print("The sum of number", n, "is", digits_sum(n))

# Write a Python program to sort files by date.
import glob
import os
files = glob.glob("*.py") # find all files in the directory with ext ".py"
files.sort(key= os.path.getmtime)
print("\n".join(files))

# Hash a word. (use a-z, no numbers)
hash = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2] # 25 digits -> A-Z has 25 indexes, because A -> 65 and Z -> 90
word = input("Input the word to be hashed: ")
word = word.upper() # only A-Z
coded = str(ord(word[0])) # initial letter, do not need to be transform to nr
for a in word[1:len(word)]:
    i = 65 - ord(a)
    coded = coded + str(hash[i])
print("Your message was coded:",coded)

# Write a Python program to find the available built-in modules.
import sys
# Import the textwrap module to format the list of module names.
import textwrap
# Get a sorted list of built-in module names in the system.
module_name = ', '.join(sorted(sys.builtin_module_names))
# Use textwrap to format the list of module names into lines with a maximum width of 70 characters.
print(textwrap.fill(module_name, width=70))

# Write a Python program to get the size of an object in bytes.
import sys
x = 0
obj = list()
obj_full = [1,2,3,"A"]
dict = {"A":"2 domy"}
string = "Ahoj"
print("The size of",x , "is", str(sys.getsizeof(x)) + " bytes.")
print("The size of",obj , "is", str(sys.getsizeof(obj)) + " bytes.")
print("The size of",obj_full , "is", str(sys.getsizeof(obj_full)) + " bytes.")
print("The size of",dict , "is", str(sys.getsizeof(dict)) + " bytes.")
print("The size of",string , "is", str(sys.getsizeof(string)) + " bytes.")

import sys 
print()  # Print a blank line for spacing
print("Current value of the recursion limit:")  # Display a message about the recursion limit
print(sys.getrecursionlimit())  # Retrieve and print the current recursion limit

# Write a Python program to get the current value of the recursion limit.
def recursive_function(n):
    if n == 0:
        return 0
    return recursive_function(n - 1) + 1
try:
    result = recursive_function(1100)  # Try a large value here
    print(f"Result: {result}")
except RecursionError:
    print("Recursion limit exceeded!")
"""