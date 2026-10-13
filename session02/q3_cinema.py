age =int(input("age: "))
day =input("day of the week:....(Saturday/Sunday/Moday/Tuesday/Wednesday/Thursday/Friday) ")

if age <5:
    price =0
elif 5<= age <=12 :
    price =50000
elif age >60:
    price =60000
else:
    price =100000
    
if day == "Tuesday":
    price =price*0.8

print(f"age: {age}")
print(f"day: {day}")

if price ==0:
    price("free")
else:
    print(f"Ticket price: {int(price)}")
