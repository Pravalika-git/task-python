# 1
num=int(input("enter the Number"))
if num>0:
    print("post")
elif num==0:
    print("zero")
elif num<0:
 print("neg")
# 2
num=int(input("Enter the number"))
if num%2==0:
    print("even")
else:
    print("odd")
#3
num=int(input("Enter the number"))
if num>=18:
    print("eligible")
else:
    print("not eligible")
#4
num1=int(input("Enter the num1"))
num2=int(input("Enter the num2"))
num3=int(input("Enter the num3"))
if num1>num2 and num1>=num3:
    print("num1 is greater",num1)
elif num2>=num1 and num2>=num3:
    print("num2 is greater",num2)
else:
    print("num3 is greater",num3)
#

if num1>num2:
    print("num1 is greater",num1)
else:
    print("num2 is greater",num2)

# 5
num=int(input("Enter the number"))
if num>=40:
    print("pass")
else:
    print("fail")
# 6

num=int(input("enter the num "))
if num==1:
    print("monday")
elif num==2:
    print("tuesday")
elif num==3:
    print("wensday")
elif num==4:
    print("thusday")
elif num==5:
    print("friday")
elif num==6:
    print("sataday")
elif num==7:
    print("sunday")


# 7
operation=input("enter operation").lower()
num1=int(input("Enter"))
num2=3
if operation=="add"or"+":
    print(num1+num2)
elif operation=="sub"or"-":
    print(num1-num2)
elif operation=="multipul"or"*":
    print(num1*num2)
elif operation=="division"or"%":
    print(num1%num2)

#8
char=input("enter a single character").lower()
if char==len(char)!=1:
    print("invalid")
else:
    if char=="aeiou":
        print("vowel")
    elif char.isalpha():
        print("consonants")
    else:
        print("speical caharcters")
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if num1>num2 and num1>=num3:
    print("num1 is greater",num1)
elif num2>=num1 and num2>=num3:
    print("num2 is greater",num2)
else:
    print("num3 is greater",num3)

#9
year=int(input("enter the number:"))
if year%4==0:
    print("it is a leap year")
elif year%400==0:
    print("it is a leap year")
elif year%100==0:
    print("it is a leap year")
else:
    print("it is not a leap year")

#10
score=int(input("enter the score:"))
if score>=90 and score<=100:
    print("Grade A")
elif score>=80 and score<=89:
    print("Gread B")
elif score>=70 and score<=79:
    print("Grade C")
elif score<=70:
    print("Fail")
elif score>100:
    print("invalid Markes")
   
#11
a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the third side"))
if a+b>c:
    print("given side are triangle")
elif a+c>b:
    print("given side are triangle")
elif b+c>a:
    print("given sides are triangle")
else:
    print("given sides are not a triangle")
