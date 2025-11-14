import produtoOOP as p #Importar o modulo
p1 = p.Produto() #Instanciar o objeto
#Entrada de dados
print("Digite os dados do produto")
p1.nome = input("\tNome:")
p1.preco = float(input("\tPreco: R$"))
p1.saldo = int(input("\tQuantidade:"))
#Saida de dados 1
print("Dados do Produto")
print(p1.dadosDoProduto())
#Adicionar Produto
q = int(input("Digite o numero de produtos a ser adicionado ao estoque"))
p1.adicionarProdutos(q)
#Saida de dados 2
print("--Dados Atualizados--")
print(p1.dadosDoProduto())
#Remover Produtos
q = int(input("Digite a o numero de produtos a ser removido do estoque"))
p1.removerProdutos(q)
#Saida de Dados 3
print("--Dados Atualizados--")
print(p1.dadosDoProduto())