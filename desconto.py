#Entrada
#Um número real positivo na primeira linha, indicando o preço da mercadoria, 
# e um número inteiro positivo na segunda linha, indicando a quantidade comprada da mercadoria.
#Saída
#Na primeira linha deve ser impresso um valor real com 
# duas casas decimais, indicando o preço da compra sem o desconto e, 
# na segunda linha, o preço final com o desconto aplicado, também com duas casas decimais.

#"Se comprar minha mercadoria concederei um desconto fixo de 10% e mais 1% a cada unidade comprada"

preco = float(input())
quantidade = float(input())
valorTotal = quantidade * preco
print(f'{valorTotal:.2f}')
valorTotalComDesconto = (valorTotal-(valorTotal*0.10+(valorTotal*quantidade*0.01)))
print(f'{valorTotalComDesconto:.2f}')