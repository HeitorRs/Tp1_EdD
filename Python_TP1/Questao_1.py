texto = "Sítio do pica-pau amarelo \n 2023"

caracteres_sem_espacos = [caractere for caractere in texto if not caractere.isspace()]

print(caracteres_sem_espacos)