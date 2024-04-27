# #Import necessary modules
# #The basic concept of the code is learnt from "https://www.geeksforgeeks.org/how-to-check-horoscope-using-python/"
import requests 
from bs4 import BeautifulSoup
import pyfiglet
from colorama import init, Fore, Back, Style
from termcolor import colored
import sys
import os 
import time


init(autoreset=True)  # Automatically reset the style to default after each print!

def horoscope(zodiac_sign: int, day: str) -> str:

    """
    Pass the user input variables to the website.
    """ 
    url = ( 
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    return soup.find("div", class_="main-horoscope").p.text 

title = pyfiglet.figlet_format("Your Horoscope", font="slant")
print(Fore.MAGENTA + Style.BRIGHT + title)

def text_effect_fast(text):
    """

    Create a fast typing effect to improve user experience.
    """
    for letter in text:
        sys.stdout.write(letter)  
        sys.stdout.flush()        
        time.sleep(0.01)         
        if letter == "\n":
            time.sleep(0.1)       
    print()  # Ensure the output ends with a newline
    
def text_effect(text, delay=0.03):
    """
    Create a slow typing effect to improve user experience,
    """
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Ensure the output ends with a newline.

def clear_terminal():
    """
    Clears the terminal.
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system("cls" if os.name == "nt" else "clear")

def get_name():
    """
    Get user input of their name and prompts if invalid input is given.
    """
    while True:
        user_name = text_effect("\nPlease enter your name:")
        name = input(" \n").capitalize()
        if name:
            return name
        else:
            print(Fore.RED + Style.BRIGHT + 'Invalid input: "Name cannot be left blank. Please enter a valid name."\n')

def read_horoscope():

    while True:

        play_game = text_effect("\nDo you want to know your horoscope prediction: Y/N")
        play = input("\n")
        if play.lower() == 'y':
            print('\nChoose the number of your zodiac sign from below list : \n',
        "\n1. Aries (Mar 21 - Apr 19) \n", "\n2. Taurus (Apr 20 - May 20) \n", 
        "\n3. Gemini (May 21 - Jun 20) \n", "\n4. Cancer (Jun 21 - Jul 22)\n", 
        "\n5. Leo (Jul 23 - Aug 22) \n", "\n6. Virgo (Aug 23 - Sep 22) \n", 
        "\n7. Libra (Sep 23 - Oct 22) \n", "\n8. Scorpio (Oct 23 - Nov 21) \n", 
        "\n9. Sagittarius (Nov 22 - Dec 21) \n", "\n10. Capricorn (Dec 22 - Jan 19) \n", 
        "\n11. Aquarius (Jan 20 - Feb 18) \n", "\n12. Pisces (Feb 19 - Mar 20)\n") 
        return

        elif play.lower() == 'n':
            print(Fore.CYAN + Style.BRIGHT + '\nThank you for using "Your Horoscope". Hope you enjoyed.\n')
            return

        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid input: Please enter either 'Y' or 'N'")

    

def get_zodiac_1(input):

    # Zodiac dictionary to get zodiac_sign input to pass in horoscope function.
    zodiac_dict = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }

    if validate_data_for_zodiac_1(input):
        return zodiac_dict[input]
    else:
        return None

def validate_data_for_zodiac_1(value):
    """
    Inside the try, checks whether the value is integer.
    Raises ValueError if input cannot be converted into int,
    or if the value is not between 1 to 12.
    """
    try:
        int_value = int(value)
        if 1 <= int_value <= 12:
            return True
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + Style.BRIGHT + f'\nInvalid data: "Please enter a number between 1 and 12."')
        return False

def get_zodiac_2(input):

    # Zodiac dictionary to use for string literals
    zodiac_dict_2 = {
        '1': 'Aries', '2': 'Taurus', '3': 'Gemini', '4': 'Cancer', '5': 'Leo', 
        '6': 'Virgo', '7': 'Libra', '8': 'Scorpio', '9': 'Sagittarius', 
        '10': 'Capricorn', '11': 'Aquarius', '12': 'Pisces'
    }
    return zodiac_dict_2.get(input, "Invalid zodiac sign")

def get_day_input():
    """
    Gets user input of day 
    """
    day_dict = {
        '1': "yesterday", '2': "today", '3': "tomorrow"
    }

    day_user = text_effect("Input the number of the day:")
    day_input = input("\n")
    if validate_data_for_day(day_input):
        return day_dict[day_input]
    else:
        return None

def validate_data_for_day(value):
    """
    Inside the try, checks whether the value is integer.
    Raises ValueError if input cannot be converted into int,
    or if the value is not between 1 to 3.
    """
    try:
        int_value = int(value)
        if 1 <= int_value <= 3:
            return True
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + Style.BRIGHT + f'\nInvalid data: "Please enter a number between 1 and 3."\n')
        return False

def zodiac_characteristics(input):
    """
    Function to print zodiac's characteristics above prediction.
    """
    zodiac_number = int(input)
    if zodiac_number == 1:
        print(Fore.CYAN + Style.BRIGHT + "Aries are amazing! Their name says it all:\n"
                  "A for assertive\n"
                  "R for refreshing\n"
                  "I for independent\n"
                  "E for energetic\n"
                  "S for sexy\n")
        return
    elif zodiac_number == 2:
        print(Fore.CYAN + Style.BRIGHT + "Taurus are powerful! Their characteristics include:\n"
            "T for trustworthy\n"
            "A for artistic\n"
            "U for unyielding\n"
            "R for reliable\n"
            "S for sensual\n")
        return
    elif zodiac_number == 3:
        print(Fore.CYAN + Style.BRIGHT + "Gemini are great communicators! Their traits are:\n"
            "G for gregarious\n"
            "E for energetic\n"
            "M for mentally active\n"
            "I for imaginative\n"
            "N for nonconformist\n")
        return
    elif zodiac_number == 4:
        print(Fore.CYAN + Style.BRIGHT + "Cancer are caring! Their name reflects:\n"
            "C for compassionate\n"
            "A for adaptable\n"
            "N for nurturing\n"
            "C for cautious\n"
            "E for empathetic\n")
        return
    elif zodiac_number == 5:
        print(Fore.CYAN + Style.BRIGHT + "Leo are luminous! They shine with:\n"
            "L for loyal\n"
            "E for energetic\n"
            "O for outgoing\n")
        return
    elif zodiac_number == 6:
        print(Fore.CYAN + Style.BRIGHT + "Virgo are virtuous! Their virtues include:\n"
            "V for virtuous\n"
            "I for intelligent\n"
            "R for realistic\n"
            "G for grounded\n"
            "O for organized\n")
        return
    elif zodiac_number == 7:
        print(Fore.CYAN + Style.BRIGHT + "Libra are balanced! They are known for:\n"
            "L for lovable\n"
            "I for idealistic\n"
            "B for balanced\n"
            "R for reasonable\n"
            "A for aesthetic\n")
        return
    elif zodiac_number == 8:
        print(Fore.CYAN + Style.BRIGHT + "Scorpio are strong! Their strengths are:\n"
            "S for strategic\n"
            "C for charismatic\n"
            "O for observant\n"
            "R for resilient\n"
            "P for passionate\n")
        return
    elif zodiac_number == 9:
        print(Fore.CYAN + Style.BRIGHT + "Sagittarius are adventurous! Their traits are:\n"
            "S for spontaneous\n"
            "A for adventurous\n"
            "G for generous\n"
            "I for inspirational\n"
            "T for truthful\n")
        return
    elif zodiac_number == 10:
        print(Fore.CYAN + Style.BRIGHT + "Capricorn are capable! They excel in:\n"
            "C for competent\n"
            "A for ambitious\n"
            "P for practical\n"
            "R for resilient\n"
            "I for intelligent\n")
        return
    elif zodiac_number == 11:
        print(Fore.CYAN + Style.BRIGHT + "Aquarius are analytical! Known for:\n"
            "A for analytical\n"
            "Q for quirky\n"
            "U for unorthodox\n"
            "A for assertive\n"
            "R for revolutionary\n")
        return
    elif zodiac_number == 12:
        print(Fore.CYAN + Style.BRIGHT + "Pisces are profound! They are:\n"
            "P for passionate\n"
            "I for intuitive\n"
            "S for spiritual\n"
            "C for compassionate\n"
            "E for empathetic\n")
        return



def replay():

    while True:

        replay = input(Fore.GREEN + Style.BRIGHT + "\nEnter 'Y' to play again and 'N' to exit: \n")
        if replay.lower() == 'y':
            main()
            return

        elif replay.lower() == 'n':
            print(Fore.CYAN + Style.BRIGHT + '\nThank you for using "Your Horoscope". Hope you enjoyed.\n')
            return

        else:
            print(Fore.RED + Style.BRIGHT + "\nInvalid input: Please enter either 'Y' or 'N'")
            
        
        

def main():
    """
    Runs all functions
    """

    name = get_name()

    clear_terminal()

    print(Fore.BLUE + Style.BRIGHT + f"Hello {name}!")

    read_horoscope()

    clear_terminal()

    zodiac_sign = None
    while zodiac_sign is None:
        # Loops if invalid data is entered for day.
        zodiac = text_effect("\nInput your zodiac sign number:")
        zodiac_sign = input("\n")

        zodiac_1 = get_zodiac_1(zodiac_sign)
        if zodiac_1 is None:
            zodiac_sign = None
        
    
    zodiac_2 = get_zodiac_2(zodiac_sign)

    clear_terminal()

    print("\nOn which day you want to know your horoscope ?\n",
        "\n1. Yesterday\n", "\n2. Today\n", "\n3. Tomorrow\n")

    day = None
    while day is None:
        # Loops if invalid data is entered for day.
        day = get_day_input()

    clear_terminal()

    print(Fore.GREEN + Style.BRIGHT + f"\nThank you {name.upper()} for your inputs.\n\nThe prediction for your zodiac sign {zodiac_2.upper()} for {day.upper()} is as follows.\n")
    zodiac_characteristics(zodiac_sign)
    horoscope_text = horoscope(zodiac_1, day)
    print(Fore.MAGENTA + Style.BRIGHT + horoscope_text)

    replay()
    

"""
This ensures that main() is only called when the script is executed directly.
"""
if __name__ == "__main__":
    main()
    

