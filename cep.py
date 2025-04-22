import requests

address = input("Digite seu CEP: ")

def search_address(cep):
    r = requests.get (f"https://viacep.com.br/ws/{cep}/json/").json()
    if "error" in r:
        return "CEP não encontrado."
    return f"{r['logradouro']}, {r['bairro']}, {r['localidade']}, {r['uf']} "

print(search_address(address))