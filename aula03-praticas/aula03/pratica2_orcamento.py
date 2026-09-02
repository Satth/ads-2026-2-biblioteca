'''
    Leia o preço unitário de um produto como float.
    Leia a quantidade como int.
    Calcule o total e aplique 10 por cento de desconto.
    Imprima com duas casas decimais, usando f-string.
    Teste com preço 19.90 e quantidade 3.
    Imprima também preco * qtd sem formatação e compare os dois números.

'''
preco = float(input("Preço unitário: "))
qtd = int(input("Quantidade: "))

total = preco * qtd
com_desconto = total * 0.9

print(total)
print(f"Total: R$ {com_desconto:.2f}")