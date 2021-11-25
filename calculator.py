def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def muliply(x,y):
    return x*y
def divide(x,y):
    return x/y
#def derivative(x):

#def integratuin(x):

print("select operation you want to perfoam")
print("1 Add")
print("2 sub")
print("3 multiply")
print("4 divide")
#print("5 derivative")
#print("6 integratuin")

while True:
    choice=input("enter choice (1/2/3/4): ")
    if choice in ('1','2', '3', '4'):
        num1= float(input("enter first number/variable :"))
        num2= float(input("enter second number/variable :"))

        if choice == '1':
            print(num1, "+", num2, "=",add(num1, num2), "credit goes to ali faorooq")
        elif choice == '2':
            print(num1, "-", num2, "=",sub(num1,num2), "credit goes to ali faorooq")
        elif choice == '3':
            print(num1, "*", num2, "=", muliply(num1,num2), "credit goes to ali faorooq" )
        elif choice == '4':
            print(num1, '/', num2, '=',divide(num1,num2) ,"credit goes to ali faorooq")
    else:
        print("wrong input")

