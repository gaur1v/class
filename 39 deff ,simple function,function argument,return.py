def showdata():                #data ko jitna chaho utna use kr skte h showdata se
    print("hello my friend")

showdata()                     #kitna hi call kro or utna hi result paao
showdata()
#
print()
# 2  function with argument
def sum(a,b):
    print(a+b)
sum(10,20)
sum(25,50)
#
print()
#  3  Dafault parameter value
def pink(m,n=1):
    print(m+n)

pink(20)
#
print()
#  4

def holl(a):
    return(a+a)

m=holl(2)
print(m)