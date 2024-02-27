import re
m= 'PYTHON '
string='the python language is very short '
hello=re.search(m,string,re.IGNORECASE) # word ko search krta h ki konse area me h

print(hello)

print()

if hello:
    print("yes:",m)

else:
    print("no")

print()
# re.match shirf bigenar(shrue ka) no. hi show krta h
qw='the'
we='the hello is simply word'
er=re.match(qw,we)
print(er)
print()
# re.finditer
a=re.compile("hesoyam",re.IGNORECASE)
s='hesoyam is the hoster in hesoyam'
z=re.finditer(a,s)
print(z)
for i in z:
    # print(i.group())     #group word ko show krta h
    # print(i.start())     #kitni word konse no. pr h
    print(i.end())         #konse no. pr word hota h

print()

# re.fidall()    ye list ko show krta h
v=re.compile("hello",re.IGNORECASE)
b="what is the hello word in string hello"
list=re.findall(v,b)
print(list)