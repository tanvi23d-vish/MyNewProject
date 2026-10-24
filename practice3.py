from os import name


x=2
if x==2:
    print("x is equal to %d" % x)


for x in range(1,9,2):
    print(x)

for x in range(0,10):
    for y in range(0,10):
        print(x,y)


while(x<10):
    print(x)
    x=x+1

primes=[2,3,5,7]
for prime in primes:
    print(prime)


#functions
def myfunction():
    print("this is my first function")    

myfunction();

def myfunctionwithargs(a,b):
    print(a+b)


myfunctionwithargs(4,5);

def mystringfunc(mystring):
    return mystring

result=mystringfunc("hello world");

print(result)

#class and object

class Vehicle:
    name=""
    kind="car"
    color=""
    value=100.00

    def description(self):
        desc="%s is a %s %s worth $%.2f." %(self.name,self.color,self.kind,self.value)
        return desc

car1=Vehicle()
car1.name="fer"
car1.color="red"
car1.value=60000.00

car2=Vehicle()
car2.name="jump"
car2.color="blue"
car2.value=10000.00

print(car1.description())
print(car2.description())


#dictionary
mydictionary={"john":4,"jane":7,"dave":3}
mydictionary["jake"]=5
del mydictionary["dave"]
for name,age in mydictionary.items():
    print("%s is %d years old" % (name,age))

#input and output
x=int(input())
print(x)

x=input()
print(x)

#multiple inputs on one line
a,b,c=map(int,input().split())
print(a+b+c)

