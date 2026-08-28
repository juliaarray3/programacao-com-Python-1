#Regex Alfanumérico --> letras e números

import re
# |--> regular expression
codigo = input ("digite um código!")
while not re.fullmatch (r"[a-z0-9]{5}", codigo):
    codigo = input ("digite um código!")