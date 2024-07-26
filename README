# Dashboard de Horas Complementares

Este repositório contém arquivos e instruções para configurar e usar um banco de dados PostgreSQL para rastreamento de horas complementares. O projeto inclui scripts SQL para criação e inserção de dados, além de um notebook Jupyter para visualização dos dados.

## Requisitos

1. **PostgreSQL**
2. **pgAdmin**
3. **Extensão Jupyter Notebook no Visual Studio Code (VSCode)**

## Instalação

### 1. Instalar o PostgreSQL

1. Baixe o PostgreSQL [aqui](https://www.postgresql.org/download/).
2. Execute o instalador e siga as instruções.
3. Durante a instalação, defina a senha do superusuário como `root` e mantenha os nomes de usuário e banco de dados padrão.

### 2. Instalar o pgAdmin

1. Baixe o pgAdmin [aqui](https://www.pgadmin.org/download/).
2. Execute o instalador e siga as instruções.
3. Ao configurar o pgAdmin, use a senha `root` para conectar ao PostgreSQL.

### 3. Configurar o Banco de Dados

1. **Criar o Banco de Dados**

   - Abra o pgAdmin.
   - Conecte-se ao servidor PostgreSQL usando a senha `root`.
   - No painel de navegação, clique com o botão direito em "Databases" e selecione "Create" > "Database".
   - Nomeie o banco de dados como `godziny_bd` e clique em "Save".

2. **Executar Scripts SQL**

   - **Criar Estrutura do Banco de Dados:**

     - No pgAdmin, clique com o botão direito no banco de dados `godziny_bd` e selecione "Query Tool".
     - Abra o arquivo `godziny_bd-script.sql` e execute o script para criar as tabelas necessárias.

   - **Inserir Dados:**

     - No Query Tool, abra o arquivo `godziny_bd-data.sql` e execute o script para inserir os dados nas tabelas.

   - **Executar Consultas:**

     - No Query Tool, abra o arquivo `godziny_bd-query.sql` e execute as consultas conforme necessário.

### 4. Configuração do Ambiente Jupyter Notebook

1. **Instalar a Extensão Jupyter no VSCode**

   - Abra o Visual Studio Code.
   - Vá para a aba de extensões (ícone de quadrado no lado esquerdo) e procure por "Jupyter".
   - Instale a extensão Jupyter Notebook para VSCode.

2. **Executar o Notebook**

   - Abra o arquivo `consultas_teste.ipynb` no VSCode.
   - Certifique-se de que o kernel Jupyter está configurado para usar o Python.
   - Execute as células do notebook para gerar gráficos com os dados do banco de dados.

## Uso

Depois de seguir os passos acima e ter o banco de dados configurado e o ambiente Jupyter Notebook configurado, você pode começar a explorar os dados e gerar gráficos com o notebook Jupyter.

### Exemplos de Consultas

No arquivo `consultas_teste.ipynb`, você encontrará exemplos de como consultar o banco de dados e visualizar os dados em gráficos usando python. Certifique-se de ter o PostgreSQL em execução e o banco de dados `godziny_bd` configurado conforme as instruções acima.

