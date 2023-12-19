import requests

def get_categories(url):
    r = requests.get(url)
    return r.json() # Retorna una lista de diccionarios