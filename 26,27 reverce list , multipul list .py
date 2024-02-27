q=[1,2,3,4,5,6,'hello',[7,8,9],5]      #list
print([q])

print()

print(q[3])

print()

print(q[7][1])            #list ke ander list ko defind krna
s=(len(q))
print(s)

print()

for n in range (s):     #1st example
    print(n,q[n])       #n is define how many number run in this project /q[n] is define is list number
print()
for a in (q):            # list q is all data transfer to a
    print(a)
print()
w=(len(q))
print(w)
print()
# for n in range (w-1,-1,-1):  #reverce  print in list
#    print(q[n])
#

q=[1,3,4,5,6,7,89]
w=(len(q))
# print(w)
for n in range (w-1,-1,-1):    #list ko reverce me chlne ke liye
    print(q[n])

print()

w=[1,2,3,4,5,6]
e=[7,8,9,0,8]
t=(len("w"))
for a,b in zip (w,e):    #multipul list ko treat krne ke liye zip file ka use kriya
    print(a,b)

