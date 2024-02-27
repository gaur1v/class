a=[]
while True:
    c=int(input('''
    1 Push Element
    2 Pop Elements
    3 Pick Element
    4 Display Stack
    5 Exit
    '''))
    if c==1:
        n=input("Enter the value 1:-")
        a.append(n)
        print(a)
    elif c==2:
        if len(a)==0:
            print('Empty Stack')
        else:
            p=a.pop()             #(2)list se word ko delet kena
            print(p)

    elif c==3:
        if len(a)==0:
            print('Empty stack')
        else:
            print('Last stack value',a[-1])     #(3)list ki last value ko show krna
    elif c==4:
            print('Display stack',a)            #(4)puri list ko show krna
    elif c==5:
       break

