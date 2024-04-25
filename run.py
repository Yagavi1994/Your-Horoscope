import requests 
from bs4 import BeautifulSoup 

def horoscope(zodiac_sign: int, day: int) -> str: 
    url = ( 
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    ) 
    soup = BeautifulSoup(requests.get(url).content, "html.parser") 
    return soup.find("div", class_="main-horoscope").p.text 


def get_zodiac_input():

    print("\nWelcome to 'Your Horoscope' \n")

    zodiac_dict = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }

    zodiac_dict_2 = {
        '1': 'Aries', '2': 'Taurus', '3': 'Gemini', '4': 'Cancer', '5': 'Leo', '6': 'Virgo', '7': 'Libra',
        '8': 'Scorpio', '9': 'Sagittarius', '10': 'Capricorn', '11': 'Aquarius', '12': 'Pisces'
    }
    
    
    print('\nChoose the number of your zodiac sign from below list : \n',
        "\n1. Aries (Mar 21 - Apr 19) \n", "\n2. Taurus (Apr 20 - May 20) \n", 
        "\n3. Gemini (May 21 - Jun 20) \n", "\n4. Cancer (Jun 21 - Jul 22)\n", 
        "\n5. Leo (Jul 23 - Aug 22) \n", "\n6. Virgo (Aug 23 - Sep 22) \n", 
        "\n7. Libra (Sep 23 - Oct 22) \n", "\n8. Scorpio (Oct 23 - Nov 21) \n", 
        "\n9. Sagittarius (Nov 22 - Dec 21) \n", "\n10. Capricorn (Dec 22 - Jan 19) \n", 
        "\n11. Aquarius (Jan 20 - Feb 18) \n", "\n12. Pisces (Feb 19 - Mar 20)\n")

    name = input("Please enter your name: \n")
    
    zodiac_sign = input("\nInput your zodiac sign number: \n")

    zodiac_1 = zodiac_dict[zodiac_sign]

    zodiac_2 = zodiac_dict_2[zodiac_sign]

    return name, zodiac_1, zodiac_2


def get_day_input():

    day_dict = {
        '1': "yesterday", '2': "today", '3': "tomorrow"
    }
    
    print("\nOn which day you want to know your horoscope ?\n",
        "\n1. Yesterday\n", "\n2. Today\n", "\n3. Tomorrow\n") 
    
    day = day_dict[input("Input the number of the day: \n")]
    print("\n")

    return day



def main():
    """
    Run all functions
    """
    inputs = get_zodiac_input()
    day = get_day_input()
    print(f"Thank you {inputs[0].upper()} for your inputs.\n\nThe prediction for your zodiac sign {inputs[2].upper()} for {day.upper()} is as follows.\n")
    horoscope_text = horoscope(inputs[1], day)
    print(horoscope_text)

if __name__ == "__main__":
    main()
