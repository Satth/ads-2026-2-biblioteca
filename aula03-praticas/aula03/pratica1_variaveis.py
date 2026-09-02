'''
    Crie curso, semestre e turno em uma única linha, com os valores "ADS", 2 e "noite".
    Imprima os três separados por espaço.
    Troque o valor de curso e turno de lugar sem usar variável auxiliar.
    Imprima de novo e confira o resultado.
    Atribua 0 a tres contadores diferentes em uma linha só.
    Tente criar uma variável chamada for e anote a mensagem de erro

'''

curso, semestre, turno = "ADS", 2, "noite"
print(curso, semestre, turno)

curso, turno = turno, curso
print(curso, semestre, turno)

a = b = c = 0
print(a, b, c)