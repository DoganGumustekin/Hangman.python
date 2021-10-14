import random
import time
# Initial Steps to invite in the game:
print("\nWelcome Hangman\n")
name = input("Enter your name: ")
print("hello " + name + "! be ready!")
time.sleep(3)

def main():
    global oyuna_basla
    global degisken
    global kelime
    global goruntule
    global tahmin_edildi
    global uzunluk

    kelimeler = ["kader", "", "ilginç", "sarı", "kalem", "bilgisayar", "araba", "kırmızı", "şemsiye", "direnç"
        , "uzay","astronomi","biyoloji","zeka","bilim","turuncu","hastane","uçurtma","yerçekimi","zehirli"
                      ,"telaş","doktor","heyelan","çığ"]
    kelime = random.choice(kelimeler)
    uzunluk = len(kelime)
    degisken = 0
    goruntule = '_' * uzunluk
    tahmin_edildi = []
    oyuna_basla = ""

def dongu():
    global oyuna_basla
    basla = input("do you want to play again\n y=yes n=no ")
    while basla not in ["Y","y","N","n"]:
        basla = input("do you want to play again\n y=yes n=no ")
    if basla == "e":
        main()
    else:
        print("thanks for your game bye bye")
        exit()
def adam_as():
    global degisken
    global goruntule
    global kelime
    global tahmin_edildi
    global oyuna_basla
    x=5
    tahmin = input("the word you have to guess is "+ goruntule +" guess a letter!")
    tahmin=tahmin.strip()
    if len(tahmin.strip())==0 or len(tahmin.strip()) >= 2 or tahmin <= "9":
        print("wrong entry try again\n")
        adam_as()

    elif tahmin in kelime:
        tahmin_edildi.extend([tahmin])
        index = kelime.find(tahmin)
        kelime =kelime[:index] + "_" + kelime[index + 1:]
        goruntule = goruntule[:index] + tahmin + goruntule[index + 1:]
        print(goruntule + "\n")

    elif tahmin in tahmin_edildi:
        print("try again\n")
    else:
        degisken += 1
        if degisken == 1:
            time.sleep(1)
            print("   -----\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
            print("wrong guess  " + str(x-degisken) + "try again\n")
        elif degisken == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("wrong guess  " + str(x-degisken) + " try again\n")

        elif degisken == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("wrong guess " + str(x - degisken) + " try again\n")

        elif degisken == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("wrong guess " + str(x - degisken) + " You have one last chance!!\n")

        elif degisken == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("wrong guess you lost!!!!\n")
            print("correct word:", tahmin_edildi, kelime)
            dongu()
    if kelime == '_' * uzunluk:
        print("congrats guess right")
        dongu()

    elif degisken != x:
            adam_as()
main()

adam_as()
