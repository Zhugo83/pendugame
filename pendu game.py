import random

def prRed(skk): print("\033[91m{}\033[00m".format(skk))
def prGreen(skk): print("\033[92m{}\033[00m".format(skk))
def prYellow(skk): print("\033[93m{}\033[00m".format(skk))
def prLightPurple(skk): print("\033[94m{}\033[00m".format(skk))


class Game:
    def __init__(self):
        self.words = ['pomme', 'banane', 'orange', 'fraise', 'raisin', 'ananas', 'cerise', 'kiwi', 'mangue', 'poire', 'pêche', 'abricot', 'prune', 'citron', 'melon', 'framboise', 'grenade']
        self.wordtoguess = random.choice(self.words)
        self.lives = 10
        self.hidenword = ['_'] * len(self.wordtoguess)
        self.guessedword = []
        
    def checkforword(self, userguess):
        if len(userguess) == 1:  # une lettre utilise "len" pour facilement savoir combien de lettre l'user a mis
            if userguess.lower() in self.guessedword:
                prRed("You've already guessed that letter.")
                print(self.hidenword, "\nletters already used: ", self.guessedword)
            else:
                self.guessedword.append(userguess)
                if userguess.lower() in self.wordtoguess.lower():
                    for i in range(len(self.hidenword)):
                        if self.wordtoguess[i] == userguess and self.hidenword[i] != userguess:
                            self.hidenword[i] = userguess
                    prGreen("Lettre correcte !")
                    print(self.hidenword, "\nletters already used: ", self.guessedword)
                else:
                    prRed("Lettre incorrecte.")
                    print(self.hidenword, "\nletters already used: ", self.guessedword)
                    self.lives -= 1
        elif len(userguess) > 1:  # Plus qu'une lettre
            if userguess.lower() == self.wordtoguess.lower():
                prGreen("Félicitations")
                print("Vous avez deviné le mot :", self.wordtoguess)
                return "gg"
            else:
                prRed("Le mot est incorrect.")
                print(self.hidenword, "\nletters already used: ", self.guessedword)
                self.lives -= 1
        if '_' not in self.hidenword: # Termine si il y a plus de _ dans hidenword, plus simple si l'user a deja devinée toutes les lettres
            prGreen("Félicitations")
            print("Vous avez deviné le mot :", self.wordtoguess)
            return "gg"
            
    def startgamependu(self):
        while self.lives != 0:
            if not self.guessedword:
                prLightPurple("Jeux du pendu, theme fruit!, vous avez 10 vie comme un vrai pendu!")
                print(self.hidenword, "Voila le nombre de lettres a devinée bonne chance!")
            user_input = str(input("\nEnter a letter or a word: "))
            if len(user_input) == 0:
                prRed("Tapée au minimum une lettre.")
            elif test.checkforword(user_input) == "gg":
                print("BRAVO!... Exiting game...")
                break
            else:
                print("il vous reste:", self.lives, "vie avant de perdre!")
        if self.lives == 0:
            prRed("You lost!")

test=Game()
prYellow("Jeux disponible: Pendu")
ya = str(input("A quel jeux voulais vous jouée? : "))
match(ya.lower()):
    case "pendu":
        test.startgamependu()
    case _:
        print("Jeux pas listée. exiting program...")