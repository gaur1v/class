D={"hello":"namestay","abunt":"galhi dena","what":300,}
print(D["what"])

for n in D:
    print(n)         #list se key ko nikalna


    print(D[n])       #list se value ko show krna



q={
    "word":"sbth",
    "work":"kaam krna",
    "ten":10,
}
print(q.get("work"))          #isme key ki value ko nikana h
for a in q.keys():            #key ko define krna
    print(a)
for w in q.values():          #value ko show krna
    print(w)
for e,r in q.items():         #key or values dono ko defind krta h
    print(e,r)


print()




m={
    "what":"kya",
    "who":"kon",
    "why":"kyu",
}
del m['what']                   #Delet krta h dictionary ki key ko

print(m)
print(m.pop('why'))             #delet ki hoyi key ki value ko define krta h
print(m)
h=dict(name='python',sylabus='ba',code=1000,)   #dict kisi string value ko dictionary me convert krta h
print(h)
print(h["name"])



print()
w={
    "red":'laal',
    'blue':"nilha",
    'yelow':'pila',
}
w.update({"hrllo":"this is cloor"})        #dictinory me new key,value ko add krna
print(w)
print(w["hrllo"])

print()

# w.clear()                          #list ko clear krna
print(w)

print()
#  dictionary me value insert krna
w["ten"]=10
print(w)
w["red"]="yello"        #key me value ko change krna
print(w)

