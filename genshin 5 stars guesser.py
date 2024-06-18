import random

name = input("What is your name? ")

print ("Hello, " + name, "time to guess the 5-stars!")

words = ['Albedo'.upper().lower(), 'Alhaitham'.upper().lower(), 'Aloy'.upper().lower(), 
         'Arlecchino'.upper().lower(), 'Ayaka'.upper().lower(), 'Ayato'.upper().lower(), 
         'Tartaglia'.upper().lower(), 'Chiori'.upper().lower(), 'Clorinde'.upper().lower(), 
         'Cyno'.upper().lower(), 'Dehya'.upper().lower(), 'Diluc'.upper().lower(),
         'Eula'.upper().lower(), 'Furina'.upper().lower(), 'Ganyu'.upper().lower(), 
         'Hutao'.upper().lower(), 'Itto'.upper().lower(), 'Jean'.upper().lower(), 
         'Kazuha'.upper().lower(),'Keqing'.upper().lower(),'Klee'.upper().lower(), 
         'Kokomi'.upper().lower(), 'Lyney'.upper().lower(),'Mona'.upper().lower(), 
         'Navia'.upper().lower(), 'Nahida'.upper().lower(),'Neuvillette'.upper().lower(), 
         'Nilou'.upper().lower(), 'Qiqi'.upper().lower(), 'Raiden'.upper().lower(), 'Shenhe'.upper().lower(), 
         'Sigewinne'.upper().lower(), 'Tighnari'.upper().lower(), 'Venti'.upper().lower(), 
         'Wanderder'.upper().lower(), 'Wriothesley'.upper().lower(),'Xianyun'.upper().lower(), 
         'Xiao'.upper().lower(), 'YaeMiko'.upper().lower(), 'Yelan'.upper().lower(), 
         'Yoimiya'.upper().lower(),'Baizhu'.upper().lower(), 'Traveller'.upper().lower(), 'Zhongli'.upper().lower()]

word = random.choice(words)
 
 
print("Guess the 5-stars!")
 
guesses = ''
turns = 45

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")

        else: 
            print("_")

            failed += 1

    if failed == 0:
     print("You Win!")
     print("The word is: " +word)

     break

    print()
    guess = input("guess a character: ")
    guesses += guess 
    if guess not in word:
        turns -= 1

        print("Wrong")
        print("You have," + str(turns), 'guesses left.')
    if turns == 0:
        print("You Loose")
