q=("welcome")
w=q.find("q")         #word ko find krna word nhi milne pr -1 show hoga
print(w)

a=q.index("l")         #word nhi milne pr error show hoga
print(a)

z=(q.isalpha())       #string me alphabate hoga to (true) dega no. h to =(faulse)
print(z)

s=("124")
print(s.isdigit())    #no.=(true)   alphabate=(false)

k=("hello12334")
print(k.isalnum())    #no. or alphabate dono me hi true dega