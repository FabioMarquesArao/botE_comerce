
# Raspando Dados

🚀BOT que pega os dados de todos os computadores do link em questao, armazena em um arquivo csv e tráz os valores em ordem crescente.


## Referência

 - [Pandas](https://pandas.pydata.org/docs/)
 - [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 - [Python](https://www.python.org/downloads/release/python-3100/)

## Apêndice



O Bot utiliza o [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/) para coletar os dados dos notebooks ( Título, descrição, preço, avaliação e estrelas).
Ao iniciar o Bot ele abre o navegador na url do [www.webscraper.io/test-sites/e-commerce/static/computers/laptops](https://webscraper.io/test-sites/e-commerce/static/computers/laptops) e percorre todas as paginas com notebooks coletando os dados.
Ao final da coleta utilizando [Pandas](https://pandas.pydata.org/docs/) ele gera um dataframe, e ainda salva todos os dados em um arquivo csv, que pode ser facilmente enviada por email para um destinatario específico utilizando [Smtplib]() .
## Melhorias


Será adicionado a funcionalidade de enviar a planilha com os dados coletados por email..
## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de fabinhoarao@gmail.com


