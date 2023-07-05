# encurtadorURLN3

## 1. Visão Geral 

O projeto do encurtador de URL tem como objetivo fornecer uma solução para encurtar URLs longas em URLs 
curtas e fáceis de compartilhar. Ele foi desenvolvido utilizando a linguagem de programação Python e a estrutura web 
Flask. O sistema utiliza um banco de dados MongoDB para armazenar as URLs encurtadas e implementa uma estratégia de 
cache com o Redis para melhorar o desempenho.

## 2. Arquitetura
A arquitetura do sistema é composta por vários componentes que trabalham juntos para fornecer as funcionalidades do encurtador de URL.

### Componentes:

**Aplicação Flask**: É o componente principal do sistema, responsável por receber as requisições HTTP e fornecer as respostas adequadas. Utiliza 
as rotas definidas para encaminhar as requisições aos recursos apropriados.

**Banco de Dados MongoDB**: É utilizado para armazenar as URLs encurtadas. A aplicação Flask se conecta ao MongoDB para realizar operações de 
inserção e recuperação de URLs.

**Redis Cache**: Implementa uma estratégia de cache para melhorar o desempenho do encurtador de URL. O Redis armazena em memória cache as URLs 
encurtadas mais acessadas, evitando consultas frequentes ao banco de dados.

**API Gateway**: Exposto pela aplicação Flask, o API Gateway oferece uma interface para acessar as funcionalidades do encurtador de URL. 
É responsável por rotear as requisições para os recursos apropriados.

**Autenticação via API Key**: A autenticação é feita por meio de uma chave de API (API Key). O API Gateway verifica se a chave fornecida nas requisições 
corresponde à chave configurada no sistema antes de permitir o acesso aos recursos.

## 3. Tecnologias Utilizadas

As principais tecnologias utilizadas no desenvolvimento do encurtador de URL são:

**Python**: Linguagem de programação utilizada para implementar a lógica do sistema.

**Flask**: Framework web em Python utilizado para criar a aplicação e expor as funcionalidades através do API Gateway.

**MongoDB**: Banco de dados NoSQL utilizado para armazenar as URLs encurtadas.

**Redis**: Banco de dados em memória utilizado como cache para melhorar o desempenho. 

**Docker**: Plataforma de contêiner utilizada para empacotar a aplicação e suas dependências, facilitando a execução em diferentes ambientes.  

## 4. Instruções de Configuração e Execução
Siga as instruções abaixo para configurar e executar o projeto do encurtador de URL:

### Pré-requisitos:

- **Python 3.9** ou superior instalado  
- **MongoDB** instalado e em execução  
- **Redis** instalado e em execução  
- **Docker** instalado **(opcional)**

### Passos:

- Clone o repositório do projeto para o seu ambiente de desenvolvimento.

- Abra um terminal na pasta raiz do projeto.

- Crie um ambiente virtual para o projeto (opcional, mas recomendado):

- Execute o comando `python3 -m venv venv` para criar o ambiente virtual.

- Ative o ambiente virtual com o comando `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows).

- Instale as dependências do projeto:

- Execute o comando `pip install -r requirements.txt` para instalar as dependências listadas no arquivo requirements.txt.

- Configure as variáveis de ambiente:

- Renomeie o arquivo .env.example para .env.

- Edite o arquivo .env e defina os valores apropriados para as variáveis de ambiente, como a chave de API (API_KEY) e as informações de conexão do MongoDB e Redis.

### Execute o projeto:

- Para executar o projeto diretamente, execute o comando `python app.py`

- Para executar o projeto usando o Docker, certifique-se de ter o Docker instalado e em execução, e execute o comando `docker-compose up --build`

- O encurtador de URL estará disponível no endereço http://localhost:5000

## 5. Testes

Para testar a solução e demonstrar sua capacidade de lidar com um volume considerável de requisições, utilizamos a ferramenta JMeter. Foram criados scripts
de teste de carga que simulam um alto número de requisições ao encurtador de URL.

Os testes foram executados com diferentes cargas de trabalho, variando o número de usuários virtuais e a taxa de requisições por segundo. Foram monitorados 
métricas como tempo de resposta, taxa de sucesso das requisições e utilização de recursos do sistema.

Os resultados dos testes demonstraram que o encurtador de URL é capaz de suportar um volume considerável de requisições sem degradação significativa no desempenho.

### Conclusão
Este documento fornece uma visão geral do projeto do encurtador de URL, incluindo a arquitetura do sistema, as tecnologias utilizadas, as instruções de configuração e 
execução, os testes realizados e a apresentação do projeto.

Com base nessas informações, você estará apto a configurar, executar, testar e apresentar o encurtador de URL de forma clara e abrangente, abordando todas as 
etapas solicitadas no projeto.
