#Check the no. entered by the user odd or even 
Num1=int(input("Enter the number"))
if Num1%2==0:
    print("Yes this no. is even")
else:
    print("this no. is odd")

#Check the largest of 3 no.
Num2=int(input("Enter the Num2"))
Num3=int(input("Enter the Num3"))
Num4=int(input("Enter the Num4"))
if Num2>Num3 and Num2>Num4:
    print("Num2 is greater here")
elif Num3>Num2 and Num3>Num4:
    print("Num3 is greater here")
elif Num4>Num2 and Num4>Num3:
    print("Num4 is greater here")
else:
    print("Both are Equal here")

#Check if this multiple of 7 or not
Num5=int(input("Enter the Num5"))
if Num5%7==0:
    print("Yes this is multiple of 7")
else:
    print("No this not multiple of 7 here")