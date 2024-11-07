# 1. WAP to check if the number entered by the user is odd or even
print("check if the number entered by the user is odd or even")
num = int(input("number : "))
if(num%2==0):
    print("Even number")
else:
    print("ODD number")

# 2 WAP to find the greatest of 3 numbers entered by the user
print(" find the greatest of 3 numbers entered by the user")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a>=b and a>=c):
    print("a is largest")
elif(b>=c):
    print("b is largest")
else:
    print("c is largest")

#3 WAP to check a number is multiple of 7 or not
print("check a number is multiple of 7 or not")
num2=int(input("number is: "))
if(num2%7==0):
    print("the number is divisible by 7")
else:
    print("The numberr is not divisible by 7")