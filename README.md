# 🏦 Desafio: Criando um Sistema Bancário com Python
Projeto desenvolvido durante o bootcamp **Python AI Backend Developer** da [Digital Innovation One (DIO)](https://www.dio.me/).

O objetivo deste desafio era criar um sistema bancário simples, aplicando os conceitos iniciais de Python. O projeto foi desenvolvido em duas versões:
1.  **v1:** Uma versão procedural, com toda a lógica num único script.
2.  **v2:** Uma versão refatorada, utilizando funções para organizar melhor o código.

---

## 💻 Funcionalidades Implementadas (v1 e v2)
O sistema permite ao utilizador realizar as seguintes operações através de um menu interativo:

### [d] Depositar
* O utilizador pode depositar apenas valores positivos.
* Todos os depósitos são armazenados e listados na operação de extrato.

### [s] Sacar
O sistema impõe 3 regras de negócio para saques:
1.  **Limite de 3 saques** diários.
2.  **Limite de R$ 500,00** por valor de saque.
3.  **Saldo insuficiente:** O utilizador não pode sacar um valor superior ao seu saldo em conta.

### [e] Extrato
* Lista todas as movimentações de depósito e saque realizadas.
* Exibe o saldo atual da conta ao final da listagem.
* Caso não haja movimentações, exibe a mensagem: "Não foram realizadas movimentações."

### [q] Sair
* Encerra a execução do programa.

---

## 🛠️ Tecnologias Utilizadas
* **Python 3**

---

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Wenes11/SEU-REPOSITORIO-AQUI.git](https://github.com/Wenes11/SEU-REPOSITORIO-AQUI.git)
    ```
    *(Não te esqueças de alterar para o link do teu repositório!)*

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd SEU-REPOSITORIO-AQUI
    ```

3.  **Execute o script Python:**
    *O projeto possui duas versões. Podes salvar cada uma num ficheiro (ex: `v1_procedural.py` e `v2_funcoes.py`) e executá-las separadamente.*

    ```bash
    # Para executar a Versão 1 (Procedural)
    python v1_procedural.py

    # Para executar a Versão 2 (Com Funções)
    python v2_funcoes.py
    ```

---

## 📈 Nosso Processo de Desenvolvimento

Este projeto foi construído em duas etapas principais, seguindo a progressão do desafio.

### Versão 1: Abordagem Procedural
A primeira versão foi construída de forma direta e procedural.

1.  **Variáveis:** Definimos as variáveis iniciais no escopo global (`saldo`, `limite_por_saque`, `extrato`, `numero_saques`, `LIMITE_SAQUES_DIARIOS`).
2.  **Menu:** Criámos um *loop* `while True` que imprime o menu e captura a `opcao` do utilizador.
3.  **Lógica:** Usámos uma estrutura `if/elif/else` para tratar cada opção (`d`, `s`, `e`, `q`):
    * **Depósito:** Verificava se o `valor` era `> 0`, atualizava o `saldo` e o `extrato`.
    * **Saque:** Continha múltiplas verificações (`if/elif`) para validar as 3 regras de negócio (saldo, limite por valor, limite de saques) antes de atualizar o `saldo`, o `extrato` e o `numero_saques`.
    * **Extrato:** Verificava se a string `extrato` estava vazia e, caso contrário, imprimia o histórico e o `saldo` formatado.

### Versão 2: Refatoração com Funções
Na segunda versão, o objetivo era otimizar o código, separando as responsabilidades e tornando-o mais limpo e reutilizável.

1.  **Separação por Funções:** Refatorámos o código da v1, criando funções específicas para cada operação:
    * `depositar()`: Cuida apenas da lógica de depósito.
    * `sacar()`: Cuida apenas da lógica e validações de saque.
    * `mostrar_extrato()`: Cuida apenas da formatação e exibição do extrato.
2.  **Função Principal (`main`)**:
    * Criámos uma função `main()` que agora contém as variáveis e o *loop* `while True`.
    * O *loop* principal ficou muito mais limpo, servindo apenas para chamar a função correspondente a cada opção do menu.
3.  **Passagem de Argumentos**:
    * As funções recebem os dados de que precisam como parâmetros (ex: `saldo`, `extrato`).
    * As funções que modificam os dados (`depositar`, `sacar`) retornam os novos valores atualizados (ex: `return saldo, extrato`).
    * Adicionámos o uso de argumentos *positional-only* (`/`) e *keyword-only* (`*`) para seguir as boas práticas do Python.

---

## 👨‍💻 Autor
Feito por **João Vitor Vargas Martins**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jo%C3%A3o-vitor-vargas-martins-b67b29292/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Wenes11)
