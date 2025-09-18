estoque =  { "colar": [ 1000, 2.30],
"anel": [ 500, 0.45],
"gloss": [ 2001, 1.20],
"rimel": [ 100, 1.50],
"blush": [ 1000, 2.20],
"livro": [500, 0.44],
"celular":[200, 9.20],
"tenis":[1000, 1.50],
"xicara":[2000, 1.22],
"garrafa":[4000,3.50],
"cha":[7.30],
"mouse":[33,5.17],
"tela":[1000,5.20],         
"jogos":[1000,2.33],
"escova":[3000,8.14],
"robux":[300,1.2],
"chave":[400,2.1],
"aretes":[6000,2.7],
"boligrafos":[100,2.3],
"cucharra":[2000,1.2] }


produto = input("Digite o produto: ")
venda = [ [ produto, int(input("Digite a quantidade:")) ] ]      
total = 0
print("Vendas:\n")
if produto in estoque:
  for  operação in venda:
    produto, quantidade = operação 
    preço = estoque[produto][1] 
    custo = preço * quantidade
    print("%12s: %3d x %6.2f = %6.2f" %
		  (produto, quantidade,preço,custo))
    estoque[produto][0] -= quantidade 
    total+=custo
else:
    print("Produto não existe!")
print(" Custo total: %21.2f\n" % total)
print("Estoque:\n")
for chave, dados in estoque.items(): 
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print("Preço: %6.2f\n" % dados[1])
 