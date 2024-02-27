import json
d={
    'course_name':'python',
    'fees':1500}
f=json.dumps(d)         # dict ko str me convert krna
print(f)
print(type(f))
#
q='{"hello":"nmste","how":"kon","fees":1200}'
x=json.loads(q)       #json string  ko disnery me convert krna
print(type(x))
print(q)
# for a in x:
#     print(a,x[a])
print(x["fees"])