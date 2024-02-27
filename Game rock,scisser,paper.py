import random
p=("paper","scisser",'rock')
ov=0
cv=0
while True:
    start=int(input('''
Game start...
1 Yes 
2 No|Exit
 '''))
    if start==1:
        for i in range(1,6):
            uchoice=int(input('''
1 paper
2 scisser
3 rock
'''))
            if uchoice==1:
                over="paper"
            elif uchoice==2:
                over="scisser"
            elif uchoice==3:
                over="rock"
            cvalue=random.choice(p)
            print("your value", over)
            print("computer value",cvalue)
            if over==cvalue:
                print("Game draw")
                ov=ov+1
                cv=cv+1
            elif (over=="paper" and cvalue=="rock") or (over=="scisser" and cvalue=="paper") or (over=="rock" and cvalue=="scisser"):
                print("player win")
                ov=ov+1
            else:
                print("computer win")
                cv=cv+1
        if ov==cv:
            print("final game draw")
            print("user score",ov)
            print("computer score",cv)
        elif ov>cv:
            print("finaly player win")
            print("over score",ov)
            print("computer score",cv)
        else:
            print("finaly computer win")
            print("computer score",cv)
            print("over score",ov)
    else:
        break