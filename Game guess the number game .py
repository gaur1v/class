import random
def hangman():
    words = ['apple','banana','cherry','date','elderberry']
    word=random.choice(words)
    guessed_letter =[]
    attempts = 6
    while attempts>=0:
        # print("\n")
        for letter in word:
            if letter in guessed_letter:
                print(letter,end=" ")
            else:
                print("_",end=" ")

        guess = input("\nguess a letter:").lower()
        if guess in guessed_letter:
            print("you already guessed that letter!")
            continue
        guessed_letter.append(guess)
        if guess not in word :
            attempts -=1
            print(("wrong guess! attempts left:",attempts))
        if set(word)==set(guessed_letter):
            print("congratulation! you guessed the word:",word)
            break
    if attempts==0:
        print("game over ! the word was",word)

hangman()

