import time
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END: str = '\033[0m'

text = "   __  ___            _\n"\
       "  /  |/  /___ _____  (_)___ ______\n"\
       " / /|_/ / __ `/ __ \/ / __ `/ ___/\n"\
       "/ /  / / /_/ / / / / / /_/ / /__\n"\
       "/_/  /_/\__,_/_/ /_/_/\__,_/\___/"

red_text = TextColor.RED + text + TextColor.END
print(red_text)
red_text = TextColor.RED + "Create by Uno" + TextColor.END
print(red_text)
print("___________________________________________________")
print("Dica: não de espaço na hora de botar o nome bote -")
opcao = input("Bote o nome da pessoa que deseja procurar:")

print("procurando Instagram...")
time.sleep(1)
print("procurando Facebook...")
time.sleep(1)
print("procurando Twitter...")
time.sleep(1)
print("procurando Reddit...")
time.sleep(1)
print("procurando Tiktok...")
time.sleep(1)
print("procurando Pinterest...")
time.sleep(1)
print("procurando Snapchat...")
time.sleep(1)
print("procurando Youtube...")
time.sleep(1)
print("procurando Linkedin...")
time.sleep(1)
print("procurando Ifunny...")
time.sleep(2)
print("____________________________________________________________________________________________________________")
print("Se não aparecer seu resultado confira se escreveu direito ou tem uma conta com mesmo nome ou se ela existe:")
print("Resultados:")
print(f"https://www.instagram.com/{opcao}/")
print(f"https://www.facebook.com/{opcao}/")
print(f"https://www.twitter.com/{opcao}/")
print(f"https://www.reddit.com/{opcao}/")
print(f"https://www.ifunny.com/{opcao}/")
print(f"https://www.pinterest.com/{opcao}/")
print(f"https://www.snapchat.com/{opcao}/")
print(f"https://www.tiktok.com/{opcao}/")
print(f"https://www.youtube.com/{opcao}/")
print(f"https://br.linkedin.com/in/{opcao}")


