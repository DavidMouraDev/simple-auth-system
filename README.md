# 🔐 Sistema de Autenticação em Python com SQLite

Um sistema simples de **cadastro e login de usuários** desenvolvido em Python, utilizando o banco de dados nativo **SQLite** e criptografia de senhas com a biblioteca **hashlib**.

---

## 🎯 Funcionalidades

- **Criação Automática do Banco de Dados:** Cria o arquivo `.db` e a tabela `users` automaticamente caso não existam.
- **Cadastro de Usuários:** Validação para evitar e-mails duplicados e salvamento seguro da senha.
- **Segurança com Hash:** As senhas nunca são guardadas em texto puro; é utilizado o algoritmo de hash (SHA-256).
- **Proteção contra SQL Injection:** Consultas parametrizadas utilizando *placeholders* (`?`).
- **Autenticação / Login:** Verificação de credenciais através da comparação de hashes.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** (Nativo do Python)
- **Hashlib** (Nativo do Python)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

2. **Navegue até a pasta do projeto:**
  ```bash
  cd seu-repositorio
  ```

3.**Execute o arquivo principal:**
  ```bash
  python main.py
  ```

📝 **Licença:**
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar!
