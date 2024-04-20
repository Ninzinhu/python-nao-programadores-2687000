# resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela apenas a segunda letra da variável

print (resumo)

# Imprima na tela a idade de Paloma (resposta esperada: "46")

resumo [:6]
# Imprima na tela o trecho final da variável

resumo [31:]

# Converta todos as letras para minúsculo e imprima na tela

resumo.lower ()

# Converta todas as letras para maiúscula e imprima na tela

resumo.upper ()
print (resumo)
# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela

resumo.title ()

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela

resumo.capitalize ()

# Imprima na tela uma string utilizando uma variável, usando o recurso string format

idade = 46

print (f"Paloma é uma mulher de {idade} anos que deseja mudar de profissão, por isso está estudando 'python'.")