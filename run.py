import requests 
from bs4 import BeautifulSoup 

def horoscope(zodiac_sign: int, day: int) -> str: 
    url = ( 
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    ) 
    soup = BeautifulSoup(requests.get(url).content, "html.parser") 
    return soup.find("div", class_="main-horoscope").p.text 


if __name__ == "__main__":
    zodiac_dict = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, '11': 11, '12': 12
    }
    
    day_dict = {
        '1': "yesterday", '2': "today", '3': "tomorrow"
    }
    
    print('\nChoose the number of your zodiac sign from below list : \n',
        "1. Aries (Mar 21 - Apr 19) \n", "2. Taurus (Apr 20 - May 20) \n", 
        "3. Gemini (May 21 - Jun 20) \n", "4. Cancer (Jun 21 - Jul 22)\n", 
        "5. Leo (Jul 23 - Aug 22) \n", "6. Virgo (Aug 23 - Sep 22) \n", 
        "7. Libra (Sep 23 - Oct 22) \n", "8. Scorpio (Oct 23 - Nov 21) \n", 
        "9. Sagittarius (Nov 22 - Dec 21) \n", "10. Capricorn (Dec 22 - Jan 19) \n", 
        "11. Aquarius (Jan 20 - Feb 18) \n", "12. Pisces (Feb 19 - Mar 20)\n")
    
    zodiac_sign = zodiac_dict[input("Input your zodiac sign number: ")]
    
    print("\nOn which day you want to know your horoscope ?\n",
        "\n1. Yesterday\n", "\n2. Today\n", "\n3. Tomorrow\n") 
    
    day = day_dict[input("Input the number of the day: ")]
    print("\n")


def main():
    """
    Run all functions
    """
    print("Welcome to Your Horoscope \n")
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)


main()
