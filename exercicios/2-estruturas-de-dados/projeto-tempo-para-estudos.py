# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;

nome = input ('Qual o seu nome?')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;

total_dias = input ('Quantos dias por semana você consegue dedicar aos estudos?')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;

total_horas = input ('Quantas horas por dias você consegue se dedicar ao estudo')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;

curso = input ('Qual curso você está fazendo agora?')



# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dias = int(total_dias)
total_horas = int(total_horas)

print (f'Oi {nome} costuma estudar {total_dias} dias por semana, durante o tempo médio de {total_horas}horas. Isso significa que ela estuda em média {total_horas*total_dias} horas por semana para o curso "{curso}."')
