# Teste Engenheiro de Software/Search Elo7

## Descrição

Este projeto é um teste para a vaga de search developer da Elo7 cujo desafio é descrito no seguinte link: https://gist.github.com/elo7-developer/31c504b5a29feac2175602a2380a03b7


## Orientação/Manifesto

Tendo em vista que se trata de um teste cujo objetivo é de ter um ambiente próximo do estágio de produção desde o início serão adotadas algumas práticas na implementação do exercício:

    1. Segurança: Gerenciamento do código assinando os commits para identificar quem fez o commit ou no uso de autenticação para uso do Solr entre outras coisas
    2. Estabilidade: Isto envolve não apenas ter um certo cuidado para fixar as versões das aplicações usadas e suas dependências para evitar o uso de software que não foi testado, como também desenvolver as aplicações do exercício de forma que elas estejam sempre funcionando dado que o importante ao usuário é que ele tenha uma experiência fluida e agradável.
    3. Documentação: Documentar não apenas as versões usadas de cada aplicação importante do exercício, mas também informar como executar as aplicações, o que o código (API) faz e a motivação para o uso de cada uma delas.

Também deveria ser adotada a escalabilidade dado que um amebiente de produção precisa estar preparado para lidar com mais de um usuário ao mesmo tempo. Porém, para simplificar a realização do teste não serão habilitados recursos que proporcionem escalabilidade, como criar Solr clusters, dividir o conjunto de dados em mais de uma parte (shards), usar um web server para gerenciar requisições, etc., porque eles adicionam complexidade ao teste e o objetivo é realizar um exercício que resolva o problema de busca e que exiba conhecimentos que proporcionem desenvolver um software que seja alterável e extensível.

Além disso, apesar de se ter em mente um ambiente de produção no desenvolvimento do projeto, como será usada apenas a branch master no desenvolvimento do exercício, o projeto conterá características de ambientes de desenvolvimento e de teste.  Por exemplo, o uso de bind mounting para o compartilhamento de diretórios que contém código fonte e dados usados no exercício e os testes unitários da API. O bind mounting será removido quando o projeto estiver completo, mas os testes unitários não porque haverá apenas um container para exercutar e testar a api.


## Estrutura do projeto

O projeto foi estruturado em uma composição de dois containers Docker, um deles executando a aplicação solr, a ferramenta de busca, e o outro a api de busca usando Flask, um microframework web em Python. As principais razões de se usar dois containers neste projeto são a de garantir que as aplicações sejam executadas isolada e independentemente umas das outras, assim se ocorrer um problema em um dos containers isso não afetará o outro, além de garantir que não haverá conflito de versões de pacotes e bibliotecas necessárias para executar ambas as aplicações ao mesmo tempo.

Como as aplicações fazem uso de dados e necessitam de configurações distintas foi criado um diretório para cada uma delas tal que cada diretório contém os dados, códigos-fonte e documentações relacionados a cada aplicação. Uma estrutura simplificada do projeto pode ser visualizada abaixo.

```
search_developer_test
│   README.md
│   docker-compose.yml
└───solr_app
│   │   README.md
└───search_api
    │   README.md
```


## Instruções de build e execução dos containers

Para construir e executar os containers digite os seguintes comandos na linha de comando:

```
docker-compose build
docker-compose up -d
```

O comando `docker-compose build` é responsável por construir os containers e o comando `docker-compose up -d` inicia (_start_) os containers em background.

<!-- # docker-compose exec app python manage.py recreate_db -->


<!-- Instruções de como build e executar os containers para testar a api e o ambiente de produção. -->


## Versões de softwares utilizados

Docker version 17.12.0-ce, build c97c6d6  
Docker compose version 1.8.0, build unknown  

<!-- Explicar brevemente o uso da API e apontar os Readme.md de cada aplicação para entender o motivo de uso das versões das aplicações, o motivo dos parâmetros usados (ser standalone, garantir eficiência e tipo de cada variável do esquema, aplicativos e versões usadas foram as últimas encontradas como estáveis e documentadas). -->

## Referências

Algumas das referências usadas para estudar a ferramentas usadas para realizar o exercício estão listadas abaixo:

http://training.play-with-docker.com  
https://docs.docker.com  
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet  
https://github.com/docker-solr/docker-solr/tree/afe43e97be7aa764656f3e0aa068bed90f6bdd27  
http://lucene.apache.org/solr/guide/7_2/  
https://medium.freecodecamp.org/docker-development-workflow-a-guide-with-flask-and-postgres-db1a1843044a  
