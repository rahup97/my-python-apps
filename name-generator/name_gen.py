#n-length name(string) generator
import random
import string

#writing down the sequences that will be required to generate a random string
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
namelist = []

def random_name_gen():
    length = int(input("What is the length of the names you would like to generate?"))
    n = int(input("How many names do you want to generate?"))
    name = ""
    for i in range(n):
        for j in range(length):
            ch = input("What should this letter be - Enter 1)v for vowel\n \t\t\t\t   2)c for consonant\n\t\t\t\t   3)Any other specific letter so that it always occurs at " + str(j+1) + " position")
            if ch == "v":
                name += random.choice(vowels)
            elif ch == "c":
                name += random.choice(consonants)
            else:
                name += ch
            if j == length-1 and i<n-1:
                print("\nNEXT NAME -\n")
        namelist.append(name)
        name=""


    for item in namelist:
        print(item)

random_name_gen()
