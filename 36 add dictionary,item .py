q={
    "hello":{"what":"about","you":"tum"},
    "this":{"is":"my","teacher":"school"}
}
print(q["hello"]["what"])
print(q["this"]["is"])

print()
w={
      "for":{"ok":"yes","did":"do"},
      "of":{"ok":"no","did":"hello"},
}
for a,b in w.items():           #for and of dono ko show krna
  print(a,b)
  print()


for m,n in w.items():
    print(m,n["ok"],n["did"])   #isme  ko (n)value ko dikane ke liye
print()
w["for"]["did"]=2000            #new value ko add krna
print(w)