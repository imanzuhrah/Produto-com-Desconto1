# Importar o módulo de produto
from catalogo import produto


# Solicita o nome e o preço
nome = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto (R$): '))

meu_produto = produto(nome, preco)

percentual = float(input('Digite o percentual de desconto (%): '))

desconto = meu_produto.aplicar_desconto(percentual)

print(f'Produto: {meu_produto.nome}')
print(f'Preço original (R$): {preco:.2f}')
print(f'Desconto (%): {desconto:.2f}')
print(f'Preço com Desconto (R$): {meu_produto.preco:.2f}')