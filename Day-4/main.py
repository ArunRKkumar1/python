# write a program to find the greatest of 3 numbers entered by the user
 
""""
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if(a >= b and a >= c):
       print ("first number is larger : ", a)
elif(b >= c):
       print ("second number is larger : ", b)
else:
       print("third number is larger : ", c)

 """

# write a program to find the lowest of 3 numbers entered by the user

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))
d = int(input("ente fourth number : "))
if(a <= b and a <= c and a<=d):
    print("first inter is lower than other : ",a)
elif(b <= c and b <= a and b <= d):
   print("second number is lower than other : ", b)
elif(c <= a and c <= b and c <= d):
    print("third is the lower than other : ",c)
else:
    print("fourth is the lowest than other : ",d)


# write to check if a number is a multiple of 7 or not