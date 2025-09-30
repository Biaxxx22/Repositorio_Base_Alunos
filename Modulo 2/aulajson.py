import json

dados_json = '{"nome" : "Bia", "idade" : 15, "cidade" : "Santana de Parnaiba"}'

dados_python = json.loads(dados_json)

print(dados_python["nome"])
print(dados_python["idade"])

pythonValue = {'isCat': False,'miceCaught': 0,'name': 'Jade','felineIQ': None,'peso': 20,'cordosolhos': 'azul','porte': 'medio','idade': 5,'pelagem': 'curta','isDog': True
}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

