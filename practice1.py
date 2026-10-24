#data types and variables
myfloat=10.0
mystring="hello"
myint=12

print(myfloat)
print(mystring)
print(myint)

myfloat=float(10);

print(myfloat);


samplelist=[]
samplelist.append(1)
samplelist.append(2)
print(samplelist)


one=1
two=3
three=one+two
print(three)

str1="hello"
str2="world"
str3=str1+str2
print(str3)

print("hello"+" "+"world")

#datatype excercise
myfloat=7.0
myint=10
mystring="hello"

if mystring=="hello":
    print("string:%s" % mystring)

if(isinstance(myfloat,float) and myfloat==7.0):
    print("myfloatis%s" % myfloat)

if isinstance(myint,int) and myint==10:
    print("myintis%s"%myint)

#list and for loop
mylist=[]
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist)

print(mylist[0])


for x in mylist:
    print(x)


mylist=["one","two","three"]
print(mylist)

lotsofhellos="hello"*10
print(lotsofhellos)

#arithmatic operator with list sorting arrays and then reversing it
even_num=[2,4,6,8]
odd_num=[1,3,5,7]
all_num=odd_num+even_num
all_num.sort()
all_num.reverse()
print(all_num)


#multiplying list with integer
print([1,2,3,4]*3)

#string functions
mystring="hello world"

print(len(mystring))
print(mystring.index("e"))
print(mystring.count("l"))
print(mystring[3:7])
print(mystring[3:7:2])

#reverse string
print(mystring[::-1])

print(mystring.reverse())