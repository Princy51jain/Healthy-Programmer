# Healthy Programmer-------------->>>>>>>>
import time
from pygame import mixer


def getdate():
    import datetime
    return datetime.datetime.now()


def eyes():
    print("Let's do some eye exercise")
    mixer.init()
    mixer.music.load("Aankhon Mein Teri Ajab Si.mp3")
    mixer.music.play(-1, 9, 14)  # here -1 is for playing the song in loop.


def water():
    print("Drink a glass full of water")
    mixer.init()
    mixer.music.load("Aaj-Blue-Hai-Pani-Pani.mp3")
    mixer.music.play(-1, 13, 20)


def exercise():
    print("Let's do some physical exercise for a healthy body")
    mixer.init()
    mixer.music.load("Kar Har Maidaan Fateh.mp3")
    mixer.music.play(-1, 45, 90)


if __name__ == '__main__':
    while True:
        time1 = str(getdate())
        name = input("enter your name : ")
        print(f"ok {name} , let's do some exercise to keep yourself healthy ")
        time.sleep(30)
        eyes()
        a = input("Enter 'Eydone' to stop...")
        if a == "Eydone":
            mixer.music.stop()
            with open("eyes.txt", "a") as f1:
                f1.write(time1 + " - done")
                f1.write("\n")
            print("Your action has been recorded in eyes.txt")
        else:
            print("Check your input!")
        water()
        b = input("Enter 'drank' to stop...")
        if b == "drank":
            mixer.music.stop()
            with open("water.txt", "a") as f1:
                f1.write(time1 + " - drank")
                f1.write("\n")
            print("Your action has been recorded in water.txt")
        else:
            print("Check your input!")
        time.sleep(15)
        exercise()
        c = input("Enter 'Exdone' to stop...")
        if c == "Exdone":
            mixer.music.stop()
            with open("exercise.txt", "a") as f1:
                f1.write(time1 + " - done")
                f1.write("\n")
            print("Your action has been recorded in exercise.txt")
        else:
            print("Check your input!")
