import random
p="qwertyuiopljhgfdsazxcvbnm!@#$%^&*(){}:"
latter=int(input("how many password to make it :-"))
passw=int(input("how many word to take in line"))
for i in range(latter):      #i= is count by number
    password=''
    for pwd in range(passw):
        password+=random.choice(p)
    print(password)
