# 🔐 SysHash — Authentication System with Bcrypt

A command-line application written in Python that demonstrates how a secure authentication system works, using bcrypt password hashing.

---

## 📋 Features

- 👤 **User registration** — creates a new user with a password securely stored as a bcrypt hash
- 🔑 **User login** — validates the provided password by comparing it against the stored hash
- 🛡️ **Secure storage** — passwords are never saved in plain text, only their hashes
- ✅ **Duplicate validation** — prevents registering an already existing username

---

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| **Python 3** | Main programming language |
| **bcrypt** | Secure password hashing with automatic salt |

---

## ⚙️ Prerequisites

```bash
pip install bcrypt
```

---

## 🚀 How to Run

```bash
python3 SysHash.py
```

The program will display an interactive menu:

```
Voce quer [C]riar-usuario [E]ntrar-usuario [S]air:
```

---

## 📤 Sample Usage

```
Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: C
Crie um nome de usuario: eduardo
Crie uma senha: mypassword123
Nome de usuario e senha salvos com sucesso!

Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: E
Digite o nome de usuario: eduardo
Digite a senha: mypassword123
Bem-vindo, eduardo!

Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: E
Digite o nome de usuario: eduardo
Digite a senha: wrongpassword
Senha invalida!
```

---

## 🧠 How bcrypt Works

Bcrypt is a hashing algorithm designed specifically for passwords. It applies a **random salt** to every generated hash, meaning two identical passwords will produce different hashes. This protects against dictionary attacks and rainbow table attacks.

```
Password: mypassword123
Hash:     $2b$12$e0NjBpVQm3...  ← never the same twice
```

---

## ⚠️ Notes

- Data is stored **in memory only** — all registered users are lost when the program exits.
- This project is an educational example of secure authentication using hashing.
- In a real-world system, hashes should be persisted in a database.

---

## 🗂️ Project Structure

```
.
├── SysHash.py     # Main source file
└── README.md      # Documentation
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
