print("HELLO VISHAL")
if 5 > 2:   #comment
 print("Five is greater than two!")
 print("hello iam Vishal and iam " ,13,  "years old")
inr =4.0 + 9 #floating value plus an integer = floating value
print(type(inr))
print(inr)
###concatenation### strings ni add cheyyali anna or else joint cheyyali anna we use concatenation examples are given below
str1 ="JOGU"
str2 = "VISHAL"
print(str1+str2) ##that gives you the output  as JOGUVISHAL without a gap between themn you need to make changes inthe print statement to get that gap 
print(str1+" "+ str2)## strings ni single quotes lo kuda store cheyyochhu
imt='vishal'
print(imt)
jv ='8'
jm ='9'
print(jv +jm )
print("what about next??")
#oka string ni and oka another class ni eppudu concatenation cheyyalemu coz python will not understand how two different classes will combile anedi so we cant combimnme two different classes
#atla chestey error vastadi
#   * this multiupliction symbol is used for three types of works 1.to multiply 2.** ni use chestey adi act as exponent 3.oka string ni * chestey that will replicate the number of times you given the number 
##example print ('vishal' *8) ani rastey we will get 8 times of the same string we given python
print('vishal'*9)#this is called as string replication  and again we cant multiply two stings also ala ayna error vastadi
##### VARIABLES#####
#   A variable is like a box in the computer’s memory where you can store a single value. If you want to use the result of an evaluated expression later in your program, you can save it inside a variable
# When a variable is assigned a new value ❸, the old value is forgotten we call it as reassigation of a variable
#RULES FOR VARIABLES
#It can’t have spaces.
#It can use only letters, numbers, and the underscore (_) character.
#It can’t begin with a number.
#It can’t be a Python keyword, such as if, for, return, or other keywords you’ll learn in this book.
#varables anevi case sensitive python is a case sensitive language 
total = 0

for i in range(1, 6):
    total += i

print(total)
marks = [85, 90, 78, 92]

highest = marks[0] #indexing antey alloting a a number for each of the letters in a specific string positve ga velthey it starts fromm 0 and if we want to give negative undecing then the last letter would start with the num -1 and continues back to the first word
for mark in marks:  #indexing ni square brackets lo indicate chestaru
    if mark > highest:
        highest = mark

print(highest)
x = 10

def change():
    x = 5
    print("Inside:", x)

change()
print("Outside:", x)
#how to take a input and print it
#if you need to get the age of the user simply add int function before the input variable as given below
vis =input("input your name:",)
age =int(input("input your age:",))
print( "my name is",vis)
print("my age is",age)
######LOOPS#####
#VERY VERY IMP TOPIC OF ALL TIME IN ANY LANGUAGE###