q=(1,2,4,6,7,8)            # tuple to convert in set
print(type(q))             # this time is tuple
l=(set(q))                 # convert
print(l)
print(type(l))             # change and convert to set

print()
# 1
w=({0,9,8,7,6})
w.add(50)           #set me koyi value ko add krna
print(w)
#
print()
# 2
w.pop()              #set me se koyi vi value ko delet kr skta h
print(w)
#
print()
# 3
w.remove(50)         #kisi spacel value ko delet krna ho exam:-50
print(w)
#
print()
# 4
w.clear()             #puri set value ko saaf krna
print(w)
#
print()
# 5
r={23,24,25,26}
r.discard(26)           #spacle value ko remove krna
print(r)
#
print()
# 6
e={11,12,13,14,15}
r=[10,24,37,49,69]
e.update(r)          #new set value ko add krna
print(e)