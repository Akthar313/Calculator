#simple calculator

def add(num1,num2):
    return num1+num2
    
def sub(num1,num2):
    return num1-num2
    
def mul(num1,num2):
    return num1*num2
    
def div(num1,num2):
    return num1/num2
    
def mod(num1,num2):
    return num1%num2
    
print("Select the operator\n"
        "1> Add\n"
        "2> Sub\n"
        "3> Mul\n"
        "4> div\n"
        "5> mod\n")
        
select = int(input("Select 1,2,3,4,5:\n"))

if(select == 1 or select == 2 or select == 3 or select == 4 or select == 5):
    x = float(input("Enter first number\n"))
    y = float(input("Enter second number\n"))
else:
    print("Invalid Operator")
    

if(select == 1):
    print(add(x,y))
elif(select == 2):
    print(sub(x,y))
elif(select == 3):
    print(mul(x,y))
elif(select == 4):
    print(div(x,y))
elif(select == 5):
    print(mod(x,y))

