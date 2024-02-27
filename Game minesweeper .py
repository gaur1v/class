
def hello(p):
    one="3" if p[0] else "_"
    two="1" if p[1] else "_"
    three="2" if p[2] else "_"
    a="2" if p[3] else "_"
    b="0" if p[4] else "_"
    c="3" if p[5] else "_"
    d="1" if p[6] else "_"
    e="0" if p[7] else "_"
    f="1" if p[8] else "_"
    g="2" if p[9] else "_"
    h="1" if p[10] else "_"
    i="3" if p[11] else "_"
    j="0" if p[12] else "_"
    k="1" if p[13] else "_"
    l="0" if p[14] else "_"
    m="3" if p[15] else "_"

    n=(f'''
{one}|{two}|{three}|{a}|
{b}|{c}|{d}|{e}|
{f}|{g}|{h}|{i}|
{j}|{k}|{l}|{m}|''')
    print((n))




q=1
if q==1:
    p = [0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0]
    # o = [0, 0, 0, 0, 0, 0]
    t=1

    while True:
        hello(p)
        if t==1:

            i=int(input('enter the value:-'))
            p[i]=1
            if i==1:
                p[0],p[1],p[2],p[5],p[6]=1,1,1,1,1
            elif i==15:
                p[14]=1
            elif i==9:
                p[8]=1
            elif i == 4 or i == 7 or i == 12 or i == 14:
                print("game over")
                break
        else:
            pass

