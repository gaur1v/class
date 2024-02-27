import time
import random
import math

def hello(xstate,zstate):
    one="x" if xstate[0] else ("y" if zstate[0] else 0)
    two="x" if xstate[1] else ("y" if zstate[1] else 1 )
    three="x" if xstate[2] else ("y" if zstate[2] else 2)
    fore="x" if xstate[3] else ("y" if zstate[3] else 3)
    five="x" if xstate[4] else ("y" if zstate[4] else 4 )
    six="x" if xstate[5] else ("y" if zstate[5] else 5)
    sevse="x" if xstate[6] else ("y" if zstate[6] else 6)
    eight="x" if xstate[7] else ("y" if zstate[7] else 7)
    nine="x" if xstate[8] else ("y" if zstate[8] else 8)
    print(f"{one}|{two}|{three}")
    print(f"{fore}|{five}|{six}")
    print(f"{sevse}|{eight}|{nine}")

number=[]
word=1
if word==1:
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("welcome to game")
    start=int(input('''
    start
    1 yes
    2 no'''))
    q = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while start==1:
        hello(xstate,zstate)

        if turn==1:
            print("x chance")
            value=int(input("please enter a value:-"))
            xstate[value]=1
            number.append(value)
            print("3 no. of list:-",number)
            if len(number)==3:
                t=math.fsum(number)
                print("3 no. of sum:-")
                if t == 3.0 or t == 12.0 or t == 21.0 or t == 9.0 or t == 15.0:
                    print("game win")
                    break


            print("count number:-",number)
            if number==3:
                print("I win")
                break

        else:
            print("z chance")
            q.remove(value)

            print("q valuse",q)
            if len(q)==0:
                print("game over")

                break

            w=random.choice(q)
            zstate[w]=1
            q.remove(w)
            print("w value",q)
            time.sleep(1)
        turn=1-turn


print(hello())
