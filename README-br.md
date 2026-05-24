# 🔐 SysHash — Sistema de Autenticação com Bcrypt

Uma aplicação de linha de comando escrita em Python que demonstra o funcionamento de um sistema de autenticação seguro, utilizando hashing de senhas com bcrypt.

---

## 📋 Funcionalidades

- 👤 **Cadastro de usuário** — cria um novo usuário com senha armazenada de forma segura via hash bcrypt
- 🔑 **Login de usuário** — valida a senha informada comparando com o hash armazenado
- 🛡️ **Armazenamento seguro** — as senhas nunca são salvas em texto puro, apenas seus hashes
- ✅ **Validação de duplicatas** — impede o cadastro de usuários já existentes

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Descrição |
|---|---|
| **Python 3** | Linguagem principal |
| **bcrypt** | Hashing seguro de senhas com salt automático |

---

## ⚙️ Pré-requisitos

```bash
pip install bcrypt
```

---

## 🚀 Como executar

```bash
python3 SysHash.py
```

O programa exibirá um menu interativo:

```
Voce quer [C]riar-usuario [E]ntrar-usuario [S]air:
```

---

## 📤 Exemplo de uso

```
Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: C
Crie um nome de usuario: eduardo
Crie uma senha: minhasenha123
Nome de usuario e senha salvos com sucesso!

Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: E
Digite o nome de usuario: eduardo
Digite a senha: minhasenha123
Bem-vindo, eduardo!

Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: E
Digite o nome de usuario: eduardo
Digite a senha: senhaerrada
Senha invalida!
```

---

## 🧠 Como funciona o bcrypt

O bcrypt é um algoritmo de hashing projetado especificamente para senhas. Ele aplica um **salt aleatório** a cada hash gerado, o que significa que duas senhas idênticas produzem hashes diferentes. Isso protege contra ataques de dicionário e rainbow tables.

```
Senha: minhasenha123
Hash:  $2b$12$e0NjBpVQm3...  ← nunca igual ao anterior
```

---

## ⚠️ Observações

- Os dados são armazenados **apenas em memória** — ao encerrar o programa, os usuários cadastrados são perdidos.
- Este projeto é um exemplo educacional de autenticação segura com hashing.
- Para um sistema real, os hashes devem ser persistidos em um banco de dados.

---

## 🗂️ Estrutura do projeto

```
.
├── SysHash.py     # Código-fonte principal
└── README.md      # Documentação
```

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
