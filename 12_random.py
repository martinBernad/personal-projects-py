import sys
from datetime import date
import datetime
from math import pi
import calendar
"""
# SPECIFIC OUTPUT
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are\n")

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
"""
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

