from requests import Session, Request
from constantes import CREDENCIAIS, URL_BASE, URL_PESQUISA, AGENT

#define a url de pesquisa
url = URL_BASE

#define os cabeçalhos
headers = {
    "User-Agent":AGENT, # seu User Agent
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    'Content-Type':'application/x-www-form-urlencoded',
    'Origin': f"{URL_BASE}",
    'Referer': f'{URL_BASE}',
    'Cache-Control': 'max-age=0',
    'Connection':'keep-alive' ,
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Site':'same-origin'
}

#instancia a sessão
s = Session()
#realiza primeiro request
response = s.get(url=url, headers=headers, verify=False)
# set os cookies
for i in response.cookies.items():
    cook = {i[0]:i[1]}
#define o body com as credenciais
payload = CREDENCIAIS # exemplo {"usuario": "xxxxx", "senha":"3333333"}
# monta o requests e prepara
req= Request("POST", url, data=payload, headers=headers, cookies=cook)
prepare = s.prepare_request(req)
#envia a solicitação
resp = s.send(prepare, verify=False)
#realiza novas pesquisar passando parametros de url
itemPesquisado = input("Qual item será pesquisado: ")
pesquisa = URL_PESQUISA + itemPesquisado
repostaPesquisa = s.get(pesquisa)
#filtra os dados com soup
from bs4 import BeautifulSoup
soup = BeautifulSoup(repostaPesquisa.content)
print(soup.prettify())
#fecha a conexão
resp.close()
repostaPesquisa.close()
s.close()

#filtra os dados especificos

# div = soup.find(id="mainContent")
# table = div.select("#mainContent > table:nth-child(3)")
# table = table[0]

# dados = []
# for tr in table.find_all('tr'):
#     td = tr.find_all('td')
#     dados.append((td[0].text, td[1].text))

# for d in dados:
#     print(d[0] + " " + d[1])
