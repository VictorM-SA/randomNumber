import random

while True:
    number = input("Pick a random number between 1 and 10.\n")
    for i in range(10):
        gen = str(random.randint(1,10))
        if(i == number):
            print("WIN You picked the same number!")
        else:
            print("LOST You did not pick the same number.\n")
            print("You picked: " + number)
            print("We picked: " + gen)
        play = input("\nWould you like to try again?\nY/N\n")
        if play == "N":
            print("Closing game.")
            quit(0)
        if play == "Y":
            print("Restarting game.")
            break
        else:
            break

