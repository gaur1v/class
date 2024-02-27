import time
import random
def hello(play,comp):

    a="x" if play[0] else ("0" if comp[0] else 0)
    b='x' if play[1] else ("0" if comp[1] else 1)
    c='x' if play[2] else ("0" if comp[2] else 2)
    d='x' if play[3] else ("0" if comp[3] else 3)
    e='x' if play[4] else ("0" if comp[4] else 4)
    f='x' if play[5] else ("0" if comp[5] else 5)
    g='x' if play[6] else ("0" if comp[6] else 6)
    h='x' if play[7] else ("0" if comp[7] else 7)
    i='x' if play[8] else ("0" if comp[8] else 8)
    print(f"{a}|{b}|{c}")
    print(f"{d}|{e}|{f}")
    print(f"{g}|{h}|{i}")
q=1
m=[0,1,2,3,4,5,6,7,8]

w=int(input('''
start game....
1 yes
2 no
'''))
if w==1:
    play=[0,0,0,0,0,0,0,0,0]
    comp=[0,0,0,0,0,0,0,0,0]

    print("The game is loding.......")
    time.sleep(3)

    while True:
        hello(play,comp)
        if q==1:
            p = int(input("enter the lovenish:-"))

            play[p]=1

            m.remove(p)
            print("m:-",m)
        else:
            # w=int(input("enter the gaurav:-"))
            print("gaurav play:-",m)

            time.sleep(3)
            w=random.choice(m)
            m.remove(w)
            print(w)
            comp[w]=2
            print(m)
        q=1-q