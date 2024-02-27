import random
print(random.randint(1,5))    #1 se lekrh 5 tkh koyi vi value dikha skta h
#
print()
#   2
print(random.randrange(1,5))     #isme last ki value show nhi hogi
#
print()
#  3
q=[1,4,6,8.9]
print(random.choice(q))     #jitni value de rhi h uthi hi show kre ga
#
print()
#    4
print(random.random())    #0 se lekr 1 tkh ki value ko show krti h
#
print()
#    5
p=[1,2,3,4,5]
(random.shuffle(p))      #koyi vi value ko kbhi bi aage ya piche la skta h
print(p)
#
print()
#    6
print(random.uniform(2,6))    #flot(point) me value show kregi