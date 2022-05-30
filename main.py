from pickletools import read_stringnl_noescape
from turtle import clear
import requests 
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


headers = {'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
url = ("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

computers = soup.find_all('div', class_="thumbnail")

#lista para receber todos os dados.
data_all = []

#laço para percorrer todas as paginas
i = 1
while True:
    new_url = (f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}")
    page = requests.get(new_url, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    computers = soup.find_all('div', class_="thumbnail")
    if computers:
        i+= 1
    else:
        break
    #laço para pegar cada computer dentro de computers    
    for computer in computers:
        data_computers = []
        title = computer.find('a', class_="title").text
        data_computers.append(title)
        price = computer.find('h4', class_="pull-right price").text 
        data_computers.append(float(price[1:])) #tratamento da variavel para float e retirada do $.
        description = computer.find('p', class_="description").text
        data_computers.append(description)
        reviews = computer.find('p', class_="pull-right").text
        data_computers.append(reviews)
        ratings = len(computer.find_all('span', class_="glyphicon glyphicon-star"))
        data_computers.append(ratings)
        data_all.append(data_computers)
#gera um dataframe com pandas       
computers_all = pd.DataFrame(data_all, columns=['title', 'price', 'description', 'reviews', 'ratings'])

#pega o dataframe e ordena em ordem crescente por preço. 
computers_all = computers_all.sort_values(by=['price'])

#gera o arquivo.csv
computers_all.to_csv('computers_all.csv', index=False)
print(computers_all)


