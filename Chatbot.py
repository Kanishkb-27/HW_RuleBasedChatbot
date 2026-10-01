import re, random
from colorama import Fore, init
init(autoreset=True)
destinations={
    "beaches":["Bali","Maldives","Phuket"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas"],
    "cities":["Tokyo","Paris","New York"]
}
jokes=[
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travellers always feel warm? Because of all their hotspot!"
]
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print("Travelbot: Do you want to go to a beach, mountain or city?")
    preference=input("You:")
    preference=normalize_input(preference)
    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(f"Travelbot: How about {suggestion}?")
        print("Travelbot: Do you like it? (yes/no)")
        answer=input("You:").lower()
        if answer=="yes":
            print(f"Travelbot: Awsome! Enjoy {suggestion}")
        elif answer=="no":
            print("Travelbot: Let's try another")
            recommend()
        else:
            print("Travelbot: I will suggest again")
            recommend()
    else:
        print("Travelbot: Sorry, I don't have that kind of destination")
        recommend()
def packing_tip():
    print("Travelbot: Where to?")
    location=input("You:")
    print("Travelbot: How many days?")
    days=input("You:")
    print(f"{Fore.GREEN}Travelbot: Packing tips for {days} days in {location}")
    print("Pack versatile clothes")
    print("Bring chargers and adaptors")
    print("Check weather forecast")
def tell_joke():
    print(f"Travelbot: {random.choice(jokes)}")
def news_updates():
    print("Science NEWS: SpaceX ISS Launch: A Falcon 9 rocket successfully launched from Cape Canaveral carrying four astronauts—two Americans, one Russian, and one Canadian—to the International Space Station.")
    print("Sports NEWS: Man City Fallout: Rival clubs and pundits are demanding severe sanctions, including potential title strippings and owner removals, following Manchester City being found guilty of Premier League financial rule breaches.")
def local_times():
    print("New York: UTC - 5")
    print("London: UTC + 0")
    print("Dar es Salaam: UTC + 3")
def show_help():
    print(f"{Fore.MAGENTA}Travelbot: I can")
    print(f"{Fore.MAGENTA}Suggest travel spots (say recommend)")
    print(f"{Fore.MAGENTA}Offer packing tips (say packing)")
    print(f"{Fore.MAGENTA}Tell a joke (say joke)")
    print(f"{Fore.MAGENTA}Give news update (say news)")
    print(f"{Fore.MAGENTA}Tell local time conversion (say time)")
    print(f"{Fore.MAGENTA}Type exit to quit")
def chat():
    print("Hi! I'm Travelbot")
    name=input("Your name?")
    print(f"Nice to meet you {name}!")
    show_help()
    while True:
        user_input=input(f"{name}")
        user_input=normalize_input(user_input)
        if user_input=="recommend":
            recommend()
        elif user_input=="packing":
            packing_tip()
        elif user_input=="joke":
            tell_joke()
        elif user_input=="news":
            news_updates()
        elif user_input=="time":
            local_times()
        elif user_input=="help":
            show_help()
        elif user_input=="exit":
            print("Travel safe")
            break
        else:
            print("Invalid input")
chat()