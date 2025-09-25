'''
import requests

response = requests.get()

print(response.status_code)
print(response.text)
'''
import requests

usuario = {
    "name": "Bia",
}

response = requests.post('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos',json = usuario)

#response.delete('https://68d00787ec1a5ff338263f44.mockapi.io/cidade/Cidadaos/11')

print(response.status_code)
print(response.json())