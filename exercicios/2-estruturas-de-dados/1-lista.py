# Crie uma lista apenas com elementos numéricos
anos = [2003, 2004, 2005, 1974]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
pessoa = ['Joao', 21 ,2003, ['phyton', 'r', 'js' , 'ruby'], True ['nadar', 'ler', 'pedalar'], False]
# Imprima na tela apenas os 5 primeiros elementos da lista
print (pessoa[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par

elementos_indice_par = pessoa [::2]
print(elementos_indice_par)
# Remova da lista o último item
pessoa.pop ()
print (pessoa)
# Insira na lista um novo item
pessoa.append('Gamer')
print(pessoa)
# Remova da lista um item específico
pessoa.remove (2003)
print (pessoa)