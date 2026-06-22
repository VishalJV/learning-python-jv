num1=int(input("Num1 "))
num2=int(input("Num2 "))
#how to choose the operating sign \
oper =input("choose the operation +  -  *  /")
if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper =="*":
    print(num1*num2)
if oper =="/":   
    if num2 == 0:
        print("can't divide with 0")
    else:
        print(num1/num2)

print("Calculation Done")
        

     