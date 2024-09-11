# Sistema Bancário em Python

Este é um simples sistema bancário em Python que permite ao usuário realizar depósitos, saques, visualizar o extrato e sair do sistema. O código simula as operações básicas de um banco, com funcionalidades limitadas e regras de negócios simples.

## Funcionalidades

- **Depósito**: Permite adicionar dinheiro ao saldo da conta.
- **Saque**: Permite sacar dinheiro do saldo, respeitando o limite diário de saques e o saldo disponível.
- **Extrato**: Exibe todas as movimentações feitas na conta, incluindo depósitos e saques.
- **Sair**: Finaliza o programa.

## Regras

1. **Depósito**: O valor deve ser positivo.
2. **Saque**:
   - O valor do saque não pode ser superior ao saldo.
   - O valor do saque não pode exceder o limite de R$ 500,00 por saque.
   - Limite de até 3 saques diários.
3. **Extrato**: Mostra as transações realizadas e o saldo atual.

## Exemplo de Uso

Ao iniciar o programa, o usuário verá o seguinte menu:

[d] Depositar [s] Sacar [e] Extrato [q] Sair


- Para realizar um depósito, o usuário seleciona a opção **[d]** e insere o valor desejado.
- Para realizar um saque, o usuário seleciona a opção **[s]** e insere o valor desejado, respeitando as regras de saldo e limite.
- Para visualizar o extrato e o saldo, o usuário seleciona a opção **[e]**.
- Para encerrar o programa, o usuário seleciona **[q]**.

## Tecnologias Utilizadas

- Linguagem: **Python 3**

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Baixe ou clone este repositório.
3. Execute o script `menu.py` em seu terminal ou IDE Python.

```bash
python menu.py

Melhorias Futuras
Adicionar a funcionalidade de limites configuráveis.
Implementar persistência de dados para salvar as movimentações.
Criar uma interface gráfica para melhorar a experiência do usuário.
Contribuição
Sinta-se à vontade para contribuir com sugestões, melhorias ou correções.


