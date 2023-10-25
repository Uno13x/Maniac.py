import time
import requests
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
print("\033[91mDica: não de espaço \033[0m")
print("\033[91mVersion 1.5 \033[0m")
print("\033[91m___________________________________________________")





def check_social_profile(platform, username):
    if platform == "instagram":
        url = f"https://www.instagram.com/{username}/"
    elif platform == "twitter":
        url = f"https://twitter.com/{username}/"
    elif platform == "youtube":
        url = f"https://www.youtube.com/@{username}/"
    elif platform == "linkedin":
        url = f"https://www.linkedin.com/in/{username}/"
    elif platform == "facebook":
        url = f"https://www.facebook.com/{username}/"
    elif platform == "snapchat":
        url = f"https://www.snapchat.com/add/{username}/"
    elif platform == "reddit":
        url = f"https://www.reddit.com/user/{username}/"
    elif platform == "tiktok":
        url = f"https://www.tiktok.com/@{username}/"
    elif platform == "pinterest":
        url = f"https://www.pinterest.com/{username}/"
    elif platform == "ifunny":
        url = f"https://ifunny.co/user/{username}/"
    else:
        return None

    response = requests.get(url)

    if response.status_code == 200:
        return url
    elif response.status_code == 404:

        return 404


platforms = ["instagram", "twitter", "youtube", "linkedin", "facebook", "snapchat", "reddit", "tiktok", "pinterest",
             "ifunny",]


username = input("\033[93mDigite o nome de usuário: \033[0m")
profile_found = False

for platform in platforms:
    result = check_social_profile(platform, username)

    if result == 404:
        print(f"\033[91mPerfil não encontrado no {platform.capitalize()} (Status 404)\033[0m")
    elif isinstance(result, str):
        print(f"\033[92mPerfil encontrado no {platform.capitalize()}: {result}\033[0m")
        profile_found = True
    else:
        print(f"\033[91mStatus do código {platform.capitalize()} (Status 404)\033[0m")


