q=[2,3,4,5,6,7,8,9]
del q[1:3]                 #delet krna list me se
print(q)
print(q.pop(5))              #pop isme clera hoyi value ko show krna
print(q)
q.remove(6)                 #kisi spacel word ko delet krna
print(q)
q.clear()             #list ko puri trh se clear krna
print(q)
q=[1,2,3,4,5,6,7,8,9]
print(q)
q[2]=24
print(q)
print()
p=[0,9,8,7,6,5,4,3,2,1]
p.insert(0,40)   #kisi vi position pr add kr skte h
print(p)
o=[10,20,30,40]                #append list ko vi add kr skta h
p.append(o)                    #list ke last me value add hoti h or squair brackit lgta h
print(p)
a=[90,80,70,60]
a.extend(o)                  #dusri list value ko bina squair brackit ke aad krta h
print(a)