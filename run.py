# #Import necessary modules
# #The basic concept of the code is learnt from "https://www.geeksforgeeks.org/how-to-check-horoscope-using-python/"
import requests 
from bs4 import BeautifulSoup 

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


print("\nWelcome to 'Your Horoscope' \n")
name = input("Please enter your name: \n")

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
    try:
        int_value = int(value)
        if 1 <= int_value <= 12:
            return True
        else:
            raise ValueError
    except ValueError:
        print(f"\nInvalid data: Please enter a number between 1 and 12.")
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
    print("\nOn which day you want to know your horoscope ?\n",
        "\n1. Yesterday\n", "\n2. Today\n", "\n3. Tomorrow\n")
    day_input = input("Input the number of the day: \n")
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
            raise ValueError("")
    except ValueError as e:
        print(f"\nInvalid data: Please enter a number between 1 and 3.")
        return False

def main():
    """
    Runs all functions
    """

    print('\nChoose the number of your zodiac sign from below list : \n',
        "\n1. Aries (Mar 21 - Apr 19) \n", "\n2. Taurus (Apr 20 - May 20) \n", 
        "\n3. Gemini (May 21 - Jun 20) \n", "\n4. Cancer (Jun 21 - Jul 22)\n", 
        "\n5. Leo (Jul 23 - Aug 22) \n", "\n6. Virgo (Aug 23 - Sep 22) \n", 
        "\n7. Libra (Sep 23 - Oct 22) \n", "\n8. Scorpio (Oct 23 - Nov 21) \n", 
        "\n9. Sagittarius (Nov 22 - Dec 21) \n", "\n10. Capricorn (Dec 22 - Jan 19) \n", 
        "\n11. Aquarius (Jan 20 - Feb 18) \n", "\n12. Pisces (Feb 19 - Mar 20)\n")

    zodiac_sign = None
    while zodiac_sign is None:
        zodiac_sign = input("\nInput your zodiac sign number: \n")
        zodiac_1 = get_zodiac_1(zodiac_sign)
        if zodiac_1 is None:
            main()
    
    zodiac_2 = get_zodiac_2(zodiac_sign)

    day = None
    while day is None:
         # Loops if invalid data is entered for day.
        day = get_day_input()
        if day is None:
            print("Please enter a valid day number.")

    print(f"\nThank you {name.upper()} for your inputs.\n\nThe prediction for your zodiac sign {zodiac_2.upper()} for {day.upper()} is as follows.\n")
    horoscope_text = horoscope(zodiac_1, day)
    print(horoscope_text)
    

if __name__ == "__main__":
    main()

