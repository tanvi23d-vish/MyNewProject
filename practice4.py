import re
class Vehicle:
    kind="car"
    name=""
    color=""
    value=100.00

    def description(self):
        desc="%s is %s %s worth %.2f." %(self.name,self.kind,self.color,self.value)
        return desc
    
car1=Vehicle()
car1.name="fer"
car1.kind="covertble"
car1.color="red"
car1.value=60000.00
print(car1.description())

car2=Vehicle()
car2.name="jump"
car2.kind="sedan"
car2.color="blue"
car2.value=10000.00

print(car2.description())


print(input("enter your personal info"))

x=(int(input("enter a number")))
print(x)

a,b,c=map(int,input("enter 3 numbers").split())
print(a,b,c)
print(a+b+c)


#Regular expressions
text="the price of item is 120.00"

pattern=r"\d+"
#find single occurance us findall function
match=re.search(pattern,text)
if match:
    print("match found", match.group())
else:
    print("match not found")

text="call me at 234-5678 or call on 345-8976"
pattern=r"\d{3}-\d{4}"

#find multiple occurences use findall function
match=re.findall(pattern,text)
print("found phone numbers",match)

#replace pattern
text="my secret code is ABC-123"
pattern=r"[A-Z]+-\d+"
clean_text=re.sub(pattern,"[RDACTED]",text)
print(clean_text)
