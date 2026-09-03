'''
    Monte um dicionário turma com Ana [8.0, 9.5], Bruno [6.0, 5.5] e Carla [4.0, 3.5].
    Percorra o dicionário com items e calcule a média de cada aluno.
    Classifique: 7 ou mais Aprovado, 5 ou mais Recuperação, abaixo disso Reprovado.
    Imprima nome, média com uma casa e situação, alinhados.
    Guarde as médias em uma lista e imprima a média da turma com duas casas.
    Extra: use sorted para listar da maior média para a menor.

'''

turma = {"Ana": [8.0, 9.5], "Bruno": [6.0, 5.5], "Carla": [4.0, 3.5]}
medias = []

for nome, notas in turma.items():
    media = sum(notas) / len(notas)
    medias.append(media)
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    print(f"{nome:<8} {media:.1f} {situacao}")

print(f"Média da turma: {sum(medias) / len(medias):.2f}")