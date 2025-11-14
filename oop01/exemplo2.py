import produtoOOP as p #Importar o modulo
p1 = p.Produto() #Instanciar o objeto
#Entrada de dados
print("Digite os dados do produto")
p1.nome = input("\tNome:")
p1.preco = float(input("\tPreco: R$"))
p1.saldo = int(input("\tQuantidade:"))
#Saida de dados 1
print("Dados do Produto")
print(f"\tNome do produto: {p1.nome}")
print(f"\tValor de compra: R$ {p1.preco}")
print(f"\tQuantidade em Estoque: R$ {p1.saldo}")
print(f"\tValor total em Estoque: {p1.valorTotalEmEstoque():.2f}")



