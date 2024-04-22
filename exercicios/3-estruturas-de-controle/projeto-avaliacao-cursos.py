# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota


cursos_linkedin = ['Introdução a SQL', 'Python: Formação Básica', 'Python para Ciência de Dados: Formação Básica', 'Descubra a Linguagem de Programação R', 'Fundamentos de Programação: Algoritmos']

curso_git = 'Git e GitHub: Formação Básica'
curso_phyton = 'Python: Formação Básica'
curso_r = 'Descubra a Linguagem de Programação R'


avaliacoes = {} #Variavel com dicionario vazio


if curso_phyton in cursos_linkedin:  #Se o curso Phyton está contido na lista de cursos_linkedin In(verificar se algo esta contido na lista)
  print(f'O curso "{curso_phyton}" está no catálogo. Por favor, avalie o curso.')
  avaliacoes[curso_phyton]= int(input('Qual é a nota que você da para o curso (De 0 a 5)?')) #Função input armazena dados do Type String(caso de amarzenar nota utiliar o método númerico int(Converte uma função para um numero inteiro))
if curso_git in cursos_linkedin:#Verificar se o curso de Git está no catalogo
  print(f' o curso "{curso_git}" está no catálogo. Por favor, avalie o curso.')
  avaliacoes[curso_git] = int(input('Qual nota você dá para esse curso (De 0 a 5)?'))
if curso_r in cursos_linkedin:
    print(f'O curso "{curso_r}" está no catálogo. Por favor, avalie o curso.')
    avaliacoes[curso_r] = int(input('Qual nota você dá para esse curso (0 a 5)?'))
else:
    print('Infelizmente o curso não compõe o nosso catálogo.')

print(avaliacoes)



