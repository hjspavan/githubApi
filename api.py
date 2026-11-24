import urllib.request
import json


def buscar_usuario(username):
    url = f"https://github.com{username}"
    req = urllib.request.Request(url, headers={"User-Agent": "github-dev-app"})
    
    with urllib.request.urlopen(req) as response:
        dados = json.loads(response.read().decode())
        print(f"Nome: {dados.get('name')}")
        print(f"Repositórios públicos: {dados.get('public_repos')}")
        print(f"Seguidores: {dados.get('followers')}")

buscar_usuario("hjspavan")
