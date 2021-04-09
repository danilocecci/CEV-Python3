import requests

try:
    url = 'http://www.pudim.com.br'
    request = requests.get(url)
except:
    print('Host inacessível')
else:
    print('Host acessível')