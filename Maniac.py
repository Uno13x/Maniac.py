import time
import requests



class TextColor:
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END: str = '\033[0m'

text ="""███▄ ▄███▓ ▄▄▄       ███▄    █  ██▓ ▄▄▄       ▄████▄  
▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▓██▒▒████▄    ▒██▀ ▀█  
▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒▒██  ▀█▄  ▒▓█    ▄ 
▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░░██▄▄▄▄██ ▒▓▓▄ ▄██▒
▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░░██░ ▓█   ▓██▒▒ ▓███▀ ░
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓   ▒▒   ▓▒█░░ ░▒ ▒  ░
░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░  ▒   ▒▒ ░  ░  ▒   
░      ░     ░   ▒      ░   ░ ░  ▒ ░  ░   ▒   ░        
       ░         ░  ░         ░  ░        ░  ░░ ░      
                                              ░         """


red_text = TextColor.RED + text + TextColor.END
print(red_text)
print("\033[91m_________________Create by unoxys 2.0______________________")





def check_social_profile(platform, username):
    if platform == "instagram":
        url = f"https://www.instagram.com/{username}/"
    elif platform == "twitter":
        url = f"https://twitter.com/{username}/"
    elif platform == "youtube":
        url = f"https://www.youtube.com/user/{username}/"
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
    elif platform == "spotify":
        url = f"https://open.spotify.com/user/{username}/"
    elif platform == "playstation":
        url = f"https://psnprofiles.com/{username}"
    elif platform == "tumblr":
        url = f"https://www.tumblr.com/{username}"
    elif platform == "shopee":
        url = f"https://shopee.com.br/{username}/"
    elif platform == "telegram":
        url = f"https://web.telegram.org/k/#@{username}"
    else:
        return None

    response = requests.get(url)

    if response.status_code == 200:
        return url
    elif response.status_code == 404:

        return 404


platforms = ["instagram", "twitter", "youtube", "linkedin", "facebook", "snapchat", "reddit", "tiktok", "pinterest",
             "ifunny", "spotify", "playstation", "tumblr", "shopee", "telegram"]


username = input("\033[31mUsername: \033[0m")
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


