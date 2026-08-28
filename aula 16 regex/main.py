import re
codigo = input ("Digite um código:")
if re.fullmatch(r"\d{4}",codigo):
    print ("código válido!")
else:
    print ("código inválido!")