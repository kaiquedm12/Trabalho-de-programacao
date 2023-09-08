# Projeto: Sistema de Gerenciamento de Padaria

Este é o projeto final da disciplina de Programação, onde desenvolvemos um sistema de gerenciamento para uma padaria. O programa foi desenvolvido na linguagem de programação Python e tem como objetivo auxiliar na gestão de produtos, vendas e geração de relatórios para uma padaria.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

### Menu Principal

O usuário tem acesso a um menu principal com as seguintes opções:
1. Cadastrar Produto.
2. Alterar Produto.
3. Realizar Venda.
4. Relatórios.
5. Sair.

O programa só será encerrado caso o usuário escolha a opção 5 - Sair.

### Cadastro de Produto

Nessa tela, o usuário pode cadastrar um produto para venda na padaria. As informações necessárias para o cadastro são:

- Identificador do produto (gerado automaticamente).
- Nome do produto.
- Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.).
- Preço de venda.
- Estoque inicial.

Campos obrigatórios:

- Nome do produto.
- Tipo de produto.
- Preço de venda.
- Estoque inicial.

Se algum dos campos obrigatórios não for fornecido, o sistema apresentará uma mensagem de aviso e reiniciará o cadastro. Após um cadastro bem-sucedido, o sistema exibirá a mensagem "Cadastro Realizado com sucesso!".

### Realizar Venda

Nessa tela, o usuário pode registrar uma venda de um produto na padaria, selecionando o produto desejado e informando a quantidade desejada. O sistema verifica se a quantidade solicitada está disponível no estoque. Se houver estoque suficiente, o sistema registra a venda, atualiza o estoque e exibe a mensagem "Venda realizada com sucesso!". Caso contrário, informará que não há estoque suficiente.

### Alteração de Produto

O usuário pode buscar um produto pelo nome ou pelo identificador e, caso o produto seja encontrado, pode alterar os seguintes campos:

- Nome do produto.
- Tipo de produto.
- Preço de venda.
- Estoque.

Após inserir os novos dados sobre o produto, o sistema apresentará uma mensagem de confirmação de alteração.

### Relatório de Produtos

Nessa tela, o sistema apresenta as seguintes opções de relatórios:

1. Relatório de todos os produtos.
2. Relatório de vendas realizadas.

Todos os relatórios contêm um cabeçalho e são apresentados de forma tabular.

## Informações Gerais para Desenvolvimento

- Linguagem: Python.
- Equipes: No máximo 3 pessoas.
- Utilização de funções para cada tarefa (exemplo: func_cadastro, func_relatorio).
- Controle de fluxo com estruturas como FOR, WHILE, IF e ELIF.
- Uso de listas ou dicionários para armazenar informações.
- Opcional: Salvar informações em um arquivo .txt ou banco de dados.
- Opcional: Criar uma interface usando ferramentas como PyQt.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em seu sistema.
2. Clone este repositório em sua máquina.
3. Execute o arquivo principal do projeto.


 
