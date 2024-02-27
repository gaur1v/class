class democlass:
    a=10
    def __init__(self):         #construction method ko call krne ki jrurth nhi h
        print('who are you')

    def hello(self):
        print("what is your name")

    def hello1(self):
        self.c=self.a*self.a              #bina self ke function me call nhi ho skti
        print(self.c)

    def hello2(self,a,b):
       print(a+b)

obj=democlass()
obj.hello()
obj.hello1()
obj.hello2(29,66)