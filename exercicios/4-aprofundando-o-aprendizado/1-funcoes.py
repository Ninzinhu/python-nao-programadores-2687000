# Crie uma função para selecionar o curso desejado em uma trilha profissional

def seleciona_curso_trilha():
  curso = int(input(
    'Digite o número do curso que você deseja iniciar: 1 - Introdução a SQL, 2 - Python: Formação Básica: '))
  return curso


# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
def percorre_niveis_curso(curso_selecionado):
  trilha = {1: {'titulo': 'Introdução a SQL', 'total_niveis': 3}, 2: {'titulo': 'Python: Formação Básica', 'total_niveis': 7}}

cursp_atual = trilha[curso_selecionado]['titulo']
curso_nivel_atual = 1
curso_total_niveis = trilha[curso_selecionado]



# Execute as funções
curso = seleciona_curso_trilha()
percorre_niveis_curso(curso)
        