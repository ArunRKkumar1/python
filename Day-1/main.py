# Here we define variable 

name = "arun"
age = 21
email = "arunkumar2003@gmail.com"
salary = 700000 

# Here we print the variable

print(name,"\n", age, "\n", email, "\n", salary)

# Here we can very easily to identify which data type we use here

print(type(name))
print(type(age))
print(type(email))
print(type(salary))

 
 # Small example of data types

age = 21
old = False
a = None

print(type(old),(a))


# sum of two number
a = 1000
b = 500
diff = (a-b), (a+b), (a*b), (a/b)
print( diff)
 
 # Expression Execution
 # String and numeric value can operate together with *

A,B = 2,3
Txt = "arun "
print(A * Txt * B)


# String and String can operate with +

C,D ="2",3
Txt= "@"
print((C+Txt)*D)

# floor gives closest integer, which is lesser than or equal
#  to the float value.
# result of (A//B) is same as floor (A/B).

X,Z = 12,5
y=X//Z
print(y)


X,Z = -12,5
y=X//Z
print(y)

X,Z = 12,-5
y=X//Z
print(y)