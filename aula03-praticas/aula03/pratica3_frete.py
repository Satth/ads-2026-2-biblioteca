'''
    Leia o valor da compra como float.
    Leia se o cliente tem cupom, respondendo s ou n.
    Com cupom, ou acima de R$ 300, o frete é zero.
    De R$ 100 até R$ 300, o frete é R$ 8.
    Abaixo de R$ 100, o frete é R$ 15.
    Imprima o frete e o total, os dois com duas casas.

'''

valor = float(input("Valor da compra: "))
cupom = input("Tem cupom? (s/n) ").lower() == "s"

if cupom or valor > 300:
    frete = 0.0
elif valor >= 100:
    frete = 8.0
else:
    frete = 15.0
print(f"Frete: R$ {frete:.2f}")
print(f"Total: R$ {valor + frete:.2f}")