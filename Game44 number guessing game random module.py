import random
Cnumber=random.randrange(1,10)
Userinput=int(input("Enter the value:--"))
if Userinput>Cnumber:
    print("computer number",Cnumber)
    print("your gusse no. is high")
elif Cnumber>Userinput:
    print("Computer number",Cnumber)
    print("your gusse no. is low")
else:
    print("computer number",Cnumber)
    print("your gusse  number is equil ")