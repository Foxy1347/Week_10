import json
import os

def getInfo():
    """Prompt for info."""
    name = input("What is your name? ")
    address = input("What is your current address? ")
    phone = input("What is your phone number? ")
    full_info = f"{name.title()}, {address.title()}, {phone}"
    return full_info

#print(getInfo().title())
filename = ''
active = True
while active:
    filepath = input("What is the file path? You may enter quit to exit. ")
    if filepath.lower() == "quit":
        active = False
        
        try:
            with open(filename) as f:
                end = json.load(f)
                print(f"Here is the information you provided.")
                print(end.title())
        except FileNotFoundError:
            pass

    elif os.path.exists(filepath) == True:
        filename = input(f"What do you want to call the file? ")
        with open(filename, 'w') as f:
            json.dump(getInfo(), f)

    else:
        print("That directory does not exist. Please try another location.")