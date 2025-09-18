import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))
print(diz_o_tipo("Alô"))

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == int:
    return('Numero inteiro')
  elif tipo == bool:
    return('Booleano')
  elif tipo == str:
    return('String')
  elif list:
    return('Lista')
  elif tipo == float:
    return('Float')
  else:
    return(int(tipo))
print(diz_o_tipo(7))
print(diz_o_tipo(True))
print(diz_o_tipo('Hi'))
print(diz_o_tipo(4.5))

