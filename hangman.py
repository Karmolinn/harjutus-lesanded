import random
import os
print("welcome to the to the game")
words = open ("../words.txt")

sampleword = random.sample(wrods,1)

if(sampleword[0]):
    print("the length of the word is: " , len(sampleword[0]))

guesses = 0
letters_guessed = []
word = []
for x in range (len(sampleword[0])):
    word.append('_')

while guessed < 3:
    guess=input("please enter the letter you guessed")

    if(guess in sampleword[0]):
        print("the letter is in the word")
        for index, letter in enumerate(sampleword[0]):
            if letter == guess:
                word[index] =(guess)

else:
    print("the letter is in the word.")
    guesses=guesses+1
    letters_guessed.append(guess)

print("you have guessed these letters: %s"%(''.join(letters_guessed)

if ''join(word) == sampleword[0]:
    break
else:
    print("you win")
    print("you only made %i wrong guesses"%guesses)











