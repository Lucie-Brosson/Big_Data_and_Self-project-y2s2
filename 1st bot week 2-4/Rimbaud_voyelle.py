from colorama import init
from colorama import Fore

from colorama import Style, Back

init()

Test_string = "Hello I am a great big Kangourou from Wasaby"

a_letter = 'a'
e_letter = 'e'
i_letter = 'i'
u_letter = 'u'
o_letter = 'o'

def try_1 (character):

    for character in Test_string :
        if character == a_letter :
            print ('\r' + Back.BLACK + character)

        elif character == e_letter :
            print (Back.WHITE + character)

        elif character == i_letter :
            print (Back.RED + character)

        elif character == u_letter :
            print (Back.GREEN + character)

        elif character == o_letter :
            print (Back.BLUE + character)

        else :
            print (Style.RESET_ALL + character)


try_1(Test_string)
