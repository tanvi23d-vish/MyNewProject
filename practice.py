print("lets start practcing Python")
x=1
if x==1:
    print("x is equal to 1")

myfloat=7.0
print(myfloat)
myfloat=float(7)
print(myfloat)


mystring="hello"
print(mystring)
mystring='hello'
print(mystring)

one=1
two=2
three=one+two
print(three)    

hello="hello"
world="world"
helloworld="hello"+" "+"world"
print(helloworld)

a,b=4,5
print(a,b)

#list
mylist=[]
mylist.append(1)
mylist.append(2)
print(mylist)
print(mylist[0])
print(mylist[1])


numbers=[]
strings=[]
names=["ayra","mayra","sayra"]

second_name=names[1]

numbers.append(10)
numbers.append(30)
numbers.append(50)

strings.append("hi")
strings.append("hello")

print(numbers)
print(strings)

print(second_name)

#operators
operation=1+2+3+6.0
print(operation)

remainder=10%3
print(remainder)


a=10**2
b=7**3
print("square",a)
print("cube",b)


#multiplying strings
lotofhello="hello"*10
print(lotofhello)


#joining list by add operator

t=[1,2,3,]
v=[5,6,7,]
print(t+v)

#repeating list using multiplication operator
x=[1,2,3]
print(x*3)

#string formatting
name="john"
print("hello, %s!" % name)

#string functions len,index, count, upper, lower, f
# ind, replace

str="hello world"
print(len(str))
print(str.index("e"))
print(str.count("l"))  
print(str[3:7:4])


#boolean operators
name ="john"
age=30
if name == "john" and age == 30:
    print("hello john")

if name == "john" or name == "jane":
    print("hello john or jane")

#in operator
if name in ["john","jane"]:
    print("hello name is in the list")


#ifelif statement
age=10
if age < 4:
    print("your a baby")
elif age < 18:
    print("your a teenager")
else:
    print("your an adult")  

#for loop
for x in range(5):
    print(x)

for x in range(3, 5):
    print(x)

for x in range(3,8,2):
    print(x)

    #while loop

    count=0
    while count<5:
        print(count)
        count+=1

count=0
while count is True:
    print(count)
    count=count+1
    if count>=5:
        break

#print even numbers from 1 to 10
for x in range(1,10):
    if x%2==0:
        print("even number:", x)
    else:
        print("odd no:",x)

#functions
def my_func():
    print("this is my 1st func")

def my_funcarg(name,greetings):
    print("hello,%s from my function I wish ,%s" %(name,greetings))

def sum(a,b):
    return a+b

my_func()
my_funcarg("ayra","good morning")
x=sum(5,6)
print(x)