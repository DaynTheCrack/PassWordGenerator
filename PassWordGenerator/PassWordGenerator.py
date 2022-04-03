# password generator hard to break
import random

from pikepdf import PasswordError
lower_letters ="azertyuiopqsdfghjklmwxcvbn"

upper_letters = "AZERTYUIOPQSDFGHJKLMWXCVBN"

numbers = "1234567890"

symbols = "|[{#~&-`\_^@])°}+=¨$£¤%*µ!:§:/;.,?"

spe_letter = "éà"

#assemblage de tout
use_for = lower_letters + upper_letters + numbers + symbols + spe_letter
nombre = int(input("Nombre de caractères ?\n>>>"))
if type(nombre) is not int:
    raise ValueError("Tu dois rentrer un nombre !")
else:
    password ="".join(random.sample(use_for,nombre))
    dict_password = {"password" : password}
print(dict_password)
