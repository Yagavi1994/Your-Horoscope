# #Import necessary modules
# #The basic concept of the code is learnt from "https://www.geeksforgeeks.org/how-to-check-horoscope-using-python/"
import requests 
from bs4 import BeautifulSoup
import pyfiglet
from colorama import init, Fore, Back, Style
import sys
import os 
import time
from zodiacs import *


# Constant Variable for Happy Face.
HAPPY_FACE = Fore.GREEN + "⊂(◉‿◉)つ".ljust(200) + Fore.RESET

# Automatically reset the style to default after each print!
init(autoreset=True)  


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


def logo():
    """
    Applies stylings to the logo.
    """
   
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

clear_terminal()

print("\n")

logo()

print(HAPPY_FACE)

text_effect("  What is your name? (OR) Press enter if you don't want to disclose your name.\n")

user = input(Fore.BLUE + Style.BRIGHT + "  ").capitalize()


def get_name(input):
    """
    Get user input of their name and prompts if invalid input is given.
    """
    while True:

        name = input
        if name:
            return name
        else:
            name = "User"
            return name


def read_horoscope():
    """
    Asks user for their input to read horoscope or not and runs a while loop based on the choice made.
    """

    logo()

    print(HAPPY_FACE)

    name = get_name(user)

    print(Fore.BLUE + Style.BRIGHT + f"  Hello {name}!")

    play_game = text_effect("\n  Are you excited to know your zodiac's traits and horoscope?")
    print(Fore.GREEN + "\n\n  Enter 1 to know your ZODIAC'S TRAITS.\n\n  Enter 2 to know your DAILY HOROSCOPE.\n\n  Enter 3 to EXIT. ")
        
    def main_menu():

        while True:

            play = input(Fore.BLUE + Style.BRIGHT + "  ")

            if validate_data(play):

                if int(play) == 1:

                    clear_terminal()

                    text_effect_fast("\n  Choose the number of your zodiac sign from below list:\n")

                    print (Fore.GREEN + "="*80)

                    text_effect_fast("\n  1. Aries (Mar 21 - Apr 19)      7. Libra (Sep 23 - Oct 22)\n") 
                    text_effect_fast("  2. Taurus (Apr 20 - May 20)     8. Scorpio (Oct 23 - Nov 21)\n") 
                    text_effect_fast("  3. Gemini (May 21 - Jun 20)     9. Sagittarius (Nov 22 - Dec 21) \n") 
                    text_effect_fast("  4. Cancer (Jun 21 - Jul 22)     10. Capricorn (Dec 22 - Jan 19) \n") 
                    text_effect_fast("  5. Leo (Jul 23 - Aug 22)        11. Aquarius (Jan 20 - Feb 18) \n") 
                    text_effect_fast("  6. Virgo (Aug 23 - Sep 22)      12. Pisces (Feb 19 - Mar 20)\n") 

                    print (Fore.GREEN + "="*80)

                    zodiac_sign = None
                    while zodiac_sign is None:
                        # Loops if invalid data is entered for zodiac_sign.
                        zodiac = text_effect("\n  Enter your zodiac sign number:")
                        zodiac_sign = input(Fore.BLUE + Style.BRIGHT + "  ")

                    zodiac_1 = get_zodiac_1(zodiac_sign)
                    if zodiac_1 is None:
                        zodiac_sign = None

                    zodiac_2 = get_zodiac_2(zodiac_sign)

                    clear_terminal()

                    print(Fore.GREEN + f"\n  The traits of your zodiac sign {zodiac_2.upper()} are:\n")

                    print ("="*80)

                    zodiac_characteristics(zodiac_sign)

                    print("="*80)

                    replay()

                    return True
                
                elif int(play) == 2:

                    clear_terminal()

                    text_effect_fast("\n  Choose the number of your zodiac sign from below list:\n")

                    print (Fore.GREEN + "="*80)

                    text_effect_fast("\n  1. Aries (Mar 21 - Apr 19)      7. Libra (Sep 23 - Oct 22)\n") 
                    text_effect_fast("  2. Taurus (Apr 20 - May 20)     8. Scorpio (Oct 23 - Nov 21)\n") 
                    text_effect_fast("  3. Gemini (May 21 - Jun 20)     9. Sagittarius (Nov 22 - Dec 21) \n") 
                    text_effect_fast("  4. Cancer (Jun 21 - Jul 22)     10. Capricorn (Dec 22 - Jan 19) \n") 
                    text_effect_fast("  5. Leo (Jul 23 - Aug 22)        11. Aquarius (Jan 20 - Feb 18) \n") 
                    text_effect_fast("  6. Virgo (Aug 23 - Sep 22)      12. Pisces (Feb 19 - Mar 20)\n") 

                    print (Fore.GREEN + "="*80)

                    zodiac_sign = None
                    while zodiac_sign is None:
                        # Loops if invalid data is entered for zodiac_sign.
                        zodiac = text_effect("\n  Enter your zodiac sign number:")
                        zodiac_sign = input(Fore.BLUE + Style.BRIGHT + "  ")


                    zodiac_1 = get_zodiac_1(zodiac_sign)
                    if zodiac_1 is None:
                        zodiac_sign = None

                    zodiac_2 = get_zodiac_2(zodiac_sign)

                    clear_terminal()

                    text_effect_fast("\n  For which day you want to know your horoscope?\n")
                    print (Fore.GREEN + "="*80) 
                    text_effect_fast("\n  1. Yesterday\n \n  2. Today\n \n  3. Tomorrow\n")
                    print (Fore.GREEN + "="*80)

                    day = None
                    while day is None:
                        # Loops if invalid data is entered for day.
                        day = get_day_input()

                    clear_terminal()

                    print(f"\n  The horoscope for {day.upper()} for {zodiac_2.upper()} is as follows:\n")

                    print ("="*80)

                    print ("\n")

                    horoscope_text = horoscope(zodiac_1, day)

                    print(Fore.MAGENTA + Style.BRIGHT + horoscope_text)

                    print("\n")

                    print ("="*80)

                    replay()

                    return True

                elif int(play) == 3:
                    clear_terminal()
                    logo()
                    print ("="*80)
                    heart()
                    print ("="*80)
                    print(Fore.CYAN + Style.BRIGHT + '\n  Thank you for using "Your Horoscope". Hope you enjoyed and will visit again.\n')
                    print ("="*80)
                    print(Fore.YELLOW + "  Click Run Program to start again.\n")

                    return False

                else:
                    print(Fore.RED + Style.BRIGHT + "\nInvalid input: Please enter a number between 1 and 3.\n")
                    main_menu()
                        

    main_menu()
    

def get_zodiac_1(input):

    # Zodiac dictionary to get zodiac_sign input to pass in horoscope function.
    zodiac_dict = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }

    # Pass the input to find whether the input given is valid or invalid.
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
        print(Fore.RED + Style.BRIGHT + f'\n  Invalid data: "Please enter a number between 1 and 12."')
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

    day_user = text_effect("\n  Enter the number of the day:")
    day_input = input(Fore.BLUE + Style.BRIGHT + "  ")

    # Pass the input to find whether the input given is valid or invalid.
    if validate_data(day_input):
        return day_dict[day_input]
    else:
        return None

def validate_data(value):
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
        print(Fore.RED + Style.BRIGHT + f'\n  Invalid data: "Please enter a number between 1 and 3."\n')
        return False

def zodiac_characteristics(input):
    """
    Function to print zodiac's characteristics above prediction.
    """
    zodiac_number = int(input)
    if zodiac_number == 1:
        aries()
        print(Fore.CYAN + Style.BRIGHT + "  Aries are amazing! Their name says it all:\n"
                  "  A for assertive\n"
                  "  R for refreshing\n"
                  "  I for independent\n"
                  "  E for energetic\n"
                  "  S for sexy\n")
        return
    elif zodiac_number == 2:
        taurus()
        print(Fore.CYAN + Style.BRIGHT + "  Taurus are powerful! Their characteristics include:\n"
            "  T for trustworthy\n"
            "  A for artistic\n"
            "  U for unyielding\n"
            "  R for reliable\n"
            "  U for Understanding"
            "  S for sensual\n")
        return
    elif zodiac_number == 3:
        gemini()
        print(Fore.CYAN + Style.BRIGHT + "  Gemini are great communicators! Their traits are:\n"
            "  G for gregarious\n"
            "  E for energetic\n"
            "  M for mentally active\n"
            "  I for imaginative\n"
            "  N for nonconformist\n"
            "  I for intelligent\n")
        return
    elif zodiac_number == 4:
        cancer()
        print(Fore.CYAN + Style.BRIGHT + "  Cancer are caring! Their name reflects:\n"
            "  C for compassionate\n"
            "  A for adaptable\n"
            "  N for nurturing\n"
            "  C for cautious\n"
            "  E for empathetic\n"
            "  R for resilient\n")
        return
    elif zodiac_number == 5:
        leo()
        print(Fore.CYAN + Style.BRIGHT + "  Leo are luminous! They shine with:\n"
            "  L for loyal\n"
            "  E for energetic\n"
            "  O for outgoing\n")
        return
    elif zodiac_number == 6:
        virgo()
        print(Fore.CYAN + Style.BRIGHT + "  Virgo are virtuous! Their virtues include:\n"
            "  V for virtuous\n"
            "  I for intelligent\n"
            "  R for realistic\n"
            "  G for grounded\n"
            "  O for organized\n")
        return
    elif zodiac_number == 7:
        libra()
        print(Fore.CYAN + Style.BRIGHT + "  Libra are balanced! They are known for:\n"
            "  L for lovable\n"
            "  I for idealistic\n"
            "  B for balanced\n"
            "  R for reasonable\n"
            "  A for aesthetic\n")
        return
    elif zodiac_number == 8:
        scorpio()
        print(Fore.CYAN + Style.BRIGHT + "  Scorpio are strong! Their strengths are:\n"
            "  S for strategic\n"
            "  C for charismatic\n"
            "  O for observant\n"
            "  R for resilient\n"
            "  P for passionate\n")
        return
    elif zodiac_number == 9:
        sagittarius()
        print(Fore.CYAN + Style.BRIGHT + "  Sagittarius are adventurous! Their traits are:\n"
            "  S for spontaneous\n"
            "  A for adventurous\n"
            "  G for generous\n"
            "  I for inspirational\n"
            "  T for truthful\n"
            "  T for tenacious adept\n"
            "  A for admirable\n"
            "  R for responsible\n"
            "  I for idealistic\n"
            "  U for unique\n"
            "  S for sophisticated\n")
        return
    elif zodiac_number == 10:
        capricorn()
        print(Fore.CYAN + Style.BRIGHT + "  Capricorn are capable! They excel in:\n"
            "  C for competent\n"
            "  A for ambitious\n"
            "  P for practical\n"
            "  R for resilient\n"
            "  I for intelligent\n"
            "  C for caring\n"
            "  O for organized\n"
            "  R for realistic\n"
            "  N for neat\n")
        return
    elif zodiac_number == 11:
        aqurius()
        print(Fore.CYAN + Style.BRIGHT + "  Aquarius are analytical! Known for:\n"
            "  A for analytical\n"
            "  Q for quirky\n"
            "  U for unorthodox\n"
            "  A for assertive\n"
            "  R for revolutionary\n"
            "  I for intereting"
            "  U for understanding\n"
            "  S for sincere\n")
        return
    elif zodiac_number == 12:
        pisces()
        print(Fore.CYAN + Style.BRIGHT + "  Pisces are profound! They are:\n"
            "  P for passionate\n"
            "  I for intuitive\n"
            "  S for spiritual\n"
            "  C for compassionate\n"
            "  E for empathetic\n"
            "  S for sensitive\n")
        return


def replay():
    """
    Asks user whether they wanna play again and runs a while loop based on the input.
    Validates whether the input is valid or not.
    """

    while True:

        replay_enter = print(Fore.YELLOW + "\n  Enter 'Y' to go back to MAIN MENU and 'N' to EXIT:")
        replay = input(Fore.BLUE + Style.BRIGHT + "  ")
        if replay.lower() == 'y':
            clear_terminal()
            read_horoscope()
            return

        elif replay.lower() == 'n':
            clear_terminal()
            logo()
            print("="*80)
            heart()
            print ("="*80)
            print(Fore.GREEN + Style.BRIGHT + '\n  Thank you for using "Your Horoscope". Hope you enjoyed and will visit again.\n')
            print ("="*80)
            print(Fore.BLUE + "  Click Run Program to start again.")
            return

        else:
            print(Fore.RED + Style.BRIGHT + "\n  Invalid input: Please enter either 'Y' or 'N'")
            

                           

def main():
    """
    Runs all functions
    """

    name = get_name(user)

    clear_terminal()

    if not read_horoscope():
        # If read_horoscope() returns False, stop execution here
        return
    

"""
This ensures that main() is only called when the script is executed directly.
"""
if __name__ == "__main__":
    main()
    

