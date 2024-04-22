# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
nivel_atual = 1
nivel_final = 3

# Crie um while loop que imprima na tela o nível atual
while nivel_atual <= nivel_final: #Enquanto o nivel atual for menor ou igual ao nivel final
  print(f'Você avancou nível no curso. Seu nível atual é {nivel_atual}.')
  nivel_atual += 1 #A cada execução do looping vamos somar 1 a variavel nivel atual
else:
  print('Parabéns você concluiu o curso')
# Insira "else" no while loop anterior.
