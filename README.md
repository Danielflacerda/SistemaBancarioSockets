# BancoSocket

## Objetivos
Praticar aspectos básicos de comunicação entre processos na arquitetura
cliente-servidor.

## Descrição
Implementar um sistema rudimentar bancário de transações financeiras, para
saque, depósito e transferência de fundos entre contas bancárias. Os
processos clientes e o servidor devem manter seus relógios lógicos atualizados
(iniciados com valor 0) e exibir em tela cada mudança de valor dos respectivos
relógios

## Detalhamento
1. As operações de transações financeiras devem estar implementadas no
lado do servidor, mantendo contas de clientes.
2. Os clientes devem se conectar ao servidor e solicitar as requisições
desejadas, ou seja, que tipo de operações financeiras (saldo, retirada e
transferência, entre contas). Cada ciente do banco terá uma conta-corrente
vinculada a um número de RG e respectivo nome do cliente.

## Restrições
1. O programa pode ser implementado em linguagens para programação
desktop em rede, como Python, Java, C, C++ ou C#.
Obs.: De preferência em Python.
2. A comunicação entre os processos deve ser implementada usado sockets.
3. Todo o programa deve estar devidamente comentado, de modo a facilitar o
entendimento do código.
4. Entregar documentação do projeto, contendo: descrição da solução,
exemplo de utilização e cópia impressa do código.

## Como instalar e executar
1. Baixar todas as dependências do projeto;
2. Baixar o Postgres e atualizar os dados de conexão com o banco conforme configuração realizada na instalação;
3. Rodar o ~server\main.py em uma instância do VS Code;
4. Rodar o ~client\main.py em outra instância dp VS Code;
