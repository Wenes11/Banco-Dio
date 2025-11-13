# 🏦 Sistema Bancário em Python (Procedural -> Funcional -> POO)

Projeto desenvolvido durante o bootcamp **Python AI Backend Developer** da [Digital Innovation One (DIO)](https://www.dio.me/).

Este repositório documenta a evolução de um sistema bancário em Python, partindo de uma implementação simples até uma arquitetura robusta baseada em **Programação Orientada a Objetos (POO)**.

---

## 🔄 Evolução do Projeto

O código foi refatorado em três etapas principais para demonstrar diferentes paradigmas de programação:

1.  **v1 - Procedural:** Script único com fluxo sequencial e estruturas condicionais simples (`if/else`).
2.  **v2 - Funcional:** Organização do código em funções modulares (`sacar`, `depositar`, `criar_usuario`) para melhor reaproveitamento e leitura.
3.  **v3 - Orientada a Objetos (POO):** Modelagem completa utilizando classes, herança, polimorfismo, encapsulamento e classes abstratas. **(Versão Atual)**

---

## 🛠️ Funcionalidades (Versão POO)

### 👥 Gestão de Clientes (`Cliente`)
* Cadastro de novos clientes (Pessoa Física) com validação básica.
* Armazenamento de dados: Nome, CPF, Data de Nascimento e Endereço.
* Um cliente pode possuir múltiplas contas.

### 💳 Gestão de Contas (`Conta` e `ContaCorrente`)
* Criação de contas vinculadas a um cliente existente.
* Geração automática do número da conta (sequencial).
* **Regras de Negócio da Conta Corrente:**
    * Limite de Saque: R$ 500,00 por transação.
    * Limite de Saques Diários: 3 operações.

### 💰 Transações (`Transacao`)
* **Depósito:** Adição de fundos (apenas valores positivos).
* **Saque:** Retirada de fundos com validação de saldo e limites.
* **Histórico:** Registo de todas as operações com data e hora (`Historico`).

---

## 🧩 Estrutura de Classes (UML Simplificado)

A arquitetura segue o modelo proposto no desafio, com as seguintes relações:

* **Transacao (ABC):** Interface para `Saque` e `Deposito`.
* **Cliente:** Classe pai de `PessoaFisica`. Possui uma lista de `contas`.
* **Conta:** Classe pai de `ContaCorrente`. Possui um `Historico` e um `Cliente` associado.
* **Historico:** Armazena uma lista de transações realizadas.

---

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Wenes11/SEU-REPOSITORIO-AQUI.git](https://github.com/Wenes11/SEU-REPOSITORIO-AQUI.git)
    ```

2.  **Navegue até o diretório:**
    ```bash
    cd SEU-REPOSITORIO-AQUI
    ```

3.  **Execute o arquivo principal (versão POO):**
    ```bash
    python sistema_bancario_poo.py
    ```

---

## 📚 Conceitos Aplicados
* **Abstração:** Uso de classes para representar entidades do mundo real (Cliente, Conta).
* **Encapsulamento:** Proteção de atributos sensíveis (ex: `_saldo`) usando métodos de acesso e propriedades (`@property`).
* **Herança:** `ContaCorrente` herda de `Conta`; `PessoaFisica` herda de `Cliente`.
* **Polimorfismo:** O método `sacar` comporta-se de forma específica na classe filha `ContaCorrente` (verificando limites).
* **Classes Abstratas (ABC):** Definição da estrutura obrigatória para Transações.

---

## 👨‍💻 Autor
Desenvolvido por **João Vitor Vargas Martins**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joão-vitor-vargas-martins-b67b29292/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Wenes11)
