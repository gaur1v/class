import time
s=1
def hello(play,comp):
    start=int(input('''
start game..
1 yes
2 no 
'''))

    if start == 1:
        print("The game is loading...........")
        time.sleep(3)
        play=[0,0,0,0,0,0,0,0,0]
        comp=[0,0,0,0,0,0,0,0,0]
        print(len(play))


while True:
    if s == 1:
        print("welcome to game")
        print(int(input("player plz enter the number:-")))


    else:
        print("game over")
        print(int(input("computer plz enter the number:-")))

    start = 1 - start





