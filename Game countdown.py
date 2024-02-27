import time
# def hello(t):
#     while t:
#         # sec=t%60
#         # min=t//60
#         min,sec=divmod(t,60)
#         timer="oo:{:02}:{:02}".format(min,sec)
#         time.sleep(1)
#         print(timer)
#         t -= 1
#
#     print("time out")
# t=input("enter the number:-")
# hello(int(t))
#
# print()
# print("SECONED METHOD")
# print()


times=int(input("Enter the no.of time:-"))
for i in range(times,0,-1):
    hour=i//3600
    second= i%60
    min=i//60
    p=(f"{hour:02}:{min:02}:{second:02}")
    time.sleep(1)
    print(p)
print("Time up!")
