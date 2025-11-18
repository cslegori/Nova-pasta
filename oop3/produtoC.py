import produtooop as p 

#entrada de dados
print("Entre com os dados do produto")
nome = input("Nome:")
preco = float(input("Perço: R$"))
saldo = int(input("Quantidade: "))

#Instanciar o meu objeto
#ps = p.Produto(nome, preco, saldo)
ps = p.Produto(nome, preco)

#Saida de dados
print(ps.dadosDoProduto())
