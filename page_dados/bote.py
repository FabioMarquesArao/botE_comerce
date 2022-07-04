
from abc import ABC
from turtle import clear
import requests 
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd



class Bote():
    def __init__(self):

        self.i = 1
        self.headers = {'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
        self.url = url = ("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
        self.new_url = (f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={self.i}")
        self.page = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.computers = self.soup.find_all('div', class_="thumbnail")

    def pegando_dados(self):
        i = 1
        while True:
            headers = {'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
            new_url = (f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={i}")
            page = requests.get(new_url, headers=headers)
            soup = BeautifulSoup(page.content,'html.parser')
            computers = soup.find_all('div', class_="thumbnail")
           
            
            
            if computers:
                i+= 1
            else:
                break
            #laço para pegar cada computer dentro de computers    
            data_all = []
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
                Bote.gera_csv(data_all)








    def gera_csv(data_all):
       
        #gera um dataframe com pandas       
        computers_all = pd.DataFrame(data_all, columns=['title', 'price', 'description', 'reviews', 'ratings'])

        #pega o dataframe e ordena em ordem crescente por preço. 
        computers_all = computers_all.sort_values(by=['price'])

        #gera o arquivo.csv
        computers_all.to_csv('computers_all.csv', index=False)
        print(computers_all)


