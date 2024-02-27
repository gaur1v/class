# campair krna h two string me kitne word match krte h
# {intersection}
my_fav={"blue",'red','green','orange'}
her_fav={'yellow','red','purpul','green','banana'}
all_collour=my_fav .intersection(her_fav)
print((all_collour))

print()
# {|}= jo word match ho rhe h string me se hta de ta h
all_fav=my_fav | her_fav   #isme (red) or (green) ko 1 hi baar show hota h
print(all_fav)

print()
# {&}=isme siraf double word hi show hote h
all_double=my_fav&her_fav
print(all_double)