#desafio 3

import re

def validate_numero_telefone(phone_number):
   pattern = r"^\([1-9]{2}\) [9]{1}[0-9]{4}\-[0-9]{4}$"
   if re.match(pattern, phone_number):  
        print("Número de telefone válido.")
   else:
       print("Número de telefone inválido.")

phone_number = input()  

validate_numero_telefone(phone_number)