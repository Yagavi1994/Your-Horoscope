from colorama import init, Fore, Back, Style
import time
import sys


def aries():
    print(Fore.RED + Style.BRIGHT + r"""
   .-.   .-.
  (_  \ /  _)  Aries
       |
       |
""")


def taurus():
    print(Fore.RED + Style.BRIGHT + r"""
    .     .
    '.___.'      Taurus
    .'   `.
   :       :
   :       :
    `.___.'
""")


def gemini():
    print(Fore.RED + Style.BRIGHT + r"""
    ._____.
      | |        Gemini
      | |
     _|_|_
    '     '
""")


def cancer():
    print(Fore.RED + Style.BRIGHT + r"""
      .--.
     /   _`.     Cancer
    (_) ( )
   '.    /
     `--'
""")


def leo():
    print(Fore.RED + Style.BRIGHT + r"""
      .--.
     (    )       Leo
    (_)  /
        (_,
""")


def virgo():
    print(Fore.RED + Style.BRIGHT + r"""
   _
  ' `:--.--.
     |  |  |_     Virgo
     |  |  | )
     |  |  |/
          (J
""")


def libra():
    print(Fore.RED + r"""
        __
   ___.'  '.___   Libra
   ____________

""")


def scorpio():
    print(Fore.RED + Style.BRIGHT + r"""
   _
  ' `:--.--.
     |  |  |      Scorpio
     |  |  |
     |  |  |  ..,
           `---':
""")


def sagittarius():
    print(Fore.RED + Style.BRIGHT + r"""
          ...
          .':     Sagittarius
        .'
    `..'
    .'`.
""")


def capricorn():
    print(Fore.RED + Style.BRIGHT + r"""
            _
    \      /_)    Capricorn
     \    /`.
      \  /   ;
       \/ __.'
""")


def aqurius():
    print(Fore.RED + Style.BRIGHT + r"""
 .-"-._.-"-._.-   Aquarius
 .-"-._.-"-._.-
""")


def pisces():
    print(Fore.RED + Style.BRIGHT + r"""

     `-.    .-'   Pisces
        :  :
      --:--:--
        :  :
     .-'    `-.
""")


def heart():
    print(Fore.RED + Style.BRIGHT + r"""
                               .-.     .-.
                              .****. .****.
                              .*****.*****.
                               .*********.
                                .*******.
                                 .*****.
                                  .***.
                                    *
""")


def logo():

    print(Fore.MAGENTA + Style.BRIGHT + r"""
    __  __                    __  __
    \ \/ /___  __  _______   / / / /___  _________  ______________  ____  ___
     \  / __ \/ / / / ___/  / /_/ / __ \/ ___/ __ \/ ___/ ___/ __ \/ __ \/ _ \
     / / /_/ / /_/ / /     / __  / /_/ / /  / /_/ (__  ) /__/ /_/ / /_/ /  __/
    /_/\____/\__,_/_/     /_/ /_/\____/_/   \____/____/\___/\____/ .___/\___/
                                                                /_/
""")


def aries_1():
    print(Fore.RED + Style.BRIGHT + r"""
                              .-.   .-.
                              (_  \ /  _)
                                  |
                                  |




  Loading your result.





""")


def taurus_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                .     .
                                '.___.'
                                .'   `.
                               :       :
                               :       :
                                `.___.'


  Loading your result..





""")


def gemini_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                ._____.
                                  | |
                                  | |
                                 _|_|_
                                '     '



  Loading your result...





""")


def cancer_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                  .--.
                                 /   _`.
                                 (_) ( )
                               '.     /
                                  `--'



  Loading your result.





""")


def leo_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                  .--.
                                 (    )
                                (_)  /
                                    (_,




  Loading your result..





""")


def virgo_1():
    print(Fore.RED + Style.BRIGHT + r"""
                               _
                              ' `:--.--.
                                |  |  |_
                                |  |  | )
                                |  |  |/
                                      (J


  Loading your result...





""")


def libra_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                   __
                              ___.'  '.___
                              ____________





  Loading your result.





""")


def scorpio_1():
    print(Fore.RED + Style.BRIGHT + r"""
                               _
                              ' `:--.--.
                                |  |  |
                                |  |  |
                                |  |  |  ..,
                                      `---':


  Loading your result..





""")


def sagittarius_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                      ...
                                      .':
                                    .'
                                `..'
                               .'`.



  Loading your result...





""")


def capricorn_1():
    print(Fore.RED + Style.BRIGHT + r"""
                                        _
                                \      /_)
                                 \    /`.
                                  \  /   ;
                                   \/ __.'



  Loading your result.





""")


def aqurius_1():
    print(Fore.RED + Style.BRIGHT + r"""
                              .-"-._.-"-._.-
                              .-"-._.-"-._.-






  Loading your result..





""")


def pisces_1():
    print(Fore.RED + Style.BRIGHT + r"""

                                `-.    .-'
                                    :  :
                                  --:--:--
                                    :  :
                                 .-'    `-.


  Loading your result...





""")


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


def thank_you():
    print("\n")
    text_effect_fast("="*80)
    text_effect_fast("="*80)
    print("\n")
    print(Fore.CYAN + r"""
                          ═✿✿✿═════✿✿═════✿✿═════✿✿✿═
                      ════════════ ('\../') ═════════════
                        ════════════ (◕.◕) ═════════════
                      ════════════ (,,)(,,) ═════════════
                      .▀█▀.█▄█.█▀█.█▄.█.█▄▀  █▄█.█▀█.█─█
                      ─.█.─█▀█.█▀█.█.▀█.█▀▄  ─█.─█▄█.█▄█

              """)
    print("\n")
    text_effect_fast("="*80)
    text_effect_fast("="*80)
    print("\n")
    print(Fore.YELLOW + "  Click Run Program to start again.")
