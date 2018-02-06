# API de busca de filmes

## Escolhas

Para criar a API de busca de filmes foi escolhido o microframework web Flask pela sua facilidade e simplicidade para criar aplicativos web.
A escolha da versão do aplicativo adotada foi o fato de ser a última versão estável documentada pelo mantenedor do framework.

Este aplicativo não usa um banco de dados pelo fato de que o armazenamento dos dados da aplicação desenvolvida é de responsabilidade do Solr.  
A biblioteca de testes de unidade a ser usada é a unittest que faz parte dos módulos padrão do Python, pois é o módulo usado na documentação do próprio Flask [1].

## Versões das principais bibliotecas utilizadas

Os módulos necessários instalados para executar o projeto podem ser obtidos executando o comando `pip-compile > requirements.txt` que irá executar o script setup.py e obter os pacotes necessários para obter todas as dependências necessárias para instalar o Flask e o módulo de testes automatizados.

Abaixo segue uma lista apenas dos principais módulos do Python utilizados no projeto.

Flask 0.12.2  
Coverage 4.5
Flask-testing 0.6.2

## Referências usadas no uso desta biblioteca

[1] http://flask.pocoo.org/docs/0.12/testing/  
[2] https://coverage.readthedocs.io/en/coverage-4.5/  
[3] https://pythonhosted.org/Flask-Testing/  
