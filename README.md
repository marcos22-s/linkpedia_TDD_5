<div align="center">

# 📚 Linkpedia
### 🚀 Desafio de TDD — Prova do Prof. Orlando

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Django-Framework-green?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/Coverage-98%25-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge">

</div>

---

# 📖 Sobre o Projeto

O **Linkpedia** é um projeto desenvolvido como resolução da avaliação prática da **Sprint 2**, proposta pelo **Professor Orlando**, com foco na aplicação de **TDD (Test-Driven Development)** utilizando o framework Django.

O principal objetivo do desafio foi desenvolver uma aplicação completa de gerenciamento de links (**CRUD**) aplicando boas práticas de desenvolvimento, segurança e testes automatizados.

---

# 👨‍💻 Desenvolvido por

## Marcos Firmino Rodrigues

🎓 Estudante de Desenvolvimento de Software Multiplataforma pela Fatec Araras.

💻 Apaixonado por desenvolvimento back-end, automações e arquitetura de software.

---

# 🎯 Objetivos do Projeto

✅ Aplicar metodologia TDD  
✅ Desenvolver CRUD completo  
✅ Implementar autenticação de usuários  
✅ Garantir segurança das rotas  
✅ Criar testes automatizados  
✅ Alcançar alta cobertura de código  
✅ Melhorar organização e manutenção do sistema

---

# 🛠️ Funcionalidades

## 🔗 Gerenciamento de Links
- Criar links
- Editar links
- Remover links
- Listar links cadastrados

## 🔒 Segurança
- Proteção de rotas
- Controle de autenticação
- Restrições de acesso

## 🧪 Testes Automatizados
- Testes de Models
- Testes de Views
- Testes de Rotas
- Testes de Regras de Negócio

---

# 🧠 Metodologia Utilizada

O desenvolvimento foi realizado seguindo o ciclo clássico do **TDD**:

## 🔴 Red
Primeiramente foram criados os testes automatizados antes da implementação das funcionalidades.

## 🟢 Green
Após isso, foi desenvolvido o código mínimo necessário para fazer os testes passarem.

## 🔵 Refactor
Por fim, o código foi refatorado visando:
- Melhor legibilidade
- Organização
- Reaproveitamento
- Facilidade de manutenção

---

# 📊 Cobertura de Testes

Após a implementação de diversos cenários de testes, incluindo:
- Caminhos positivos
- Tratamento de erros
- Validações
- Casos extremos

Foi utilizada a biblioteca `coverage` para análise da cobertura da aplicação.

<div align="center">

# ✅ 98% de Cobertura de Código

</div>

---

# ⚙️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| 🐍 Python | Linguagem principal |
| 🌐 Django | Framework web |
| 🧪 Coverage | Cobertura de testes |
| 🗄️ SQLite | Banco de dados |
| 🎨 HTML/CSS | Interface |

---

# 📂 Estrutura do Projeto

```bash
linkpedia/
│
├── app/
├── templates/
├── static/
├── tests/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Como Executar o Projeto

## 📥 1. Clone o repositório

```bash
git clone <https://github.com/marcos22-s/linkpedia_TDD_5>
```

---

## 📁 2. Entre na pasta do projeto

```bash
cd linkpedia
```

---

## 🐍 3. Ative o ambiente virtual

### Windows
```bash
.\virtualenv\Scripts\activate
```

### Linux/macOS
```bash
source virtualenv/bin/activate
```

---

## 📦 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ 5. Execute as migrações

```bash
python manage.py migrate
```

---

## ▶️ 6. Inicie o servidor

```bash
python manage.py runserver
```

---

# 🧪 Executando os Testes

## Rodar todos os testes

```bash
python manage.py test
```

---

# 📈 Gerando Relatório de Cobertura

```bash
coverage run manage.py test
coverage report
```

## Gerar versão HTML

```bash
coverage html
```

Depois abra:

```bash
htmlcov/index.html
```

---

# 💡 Conceitos Aplicados

- ✅ Test-Driven Development
- ✅ CRUD
- ✅ Autenticação
- ✅ Segurança de rotas
- ✅ Cobertura de testes
- ✅ Organização de código
- ✅ Refatoração
- ✅ Boas práticas de desenvolvimento

---

# 📸 Resultado do Projeto

O projeto foi desenvolvido com foco em:
- Qualidade de software
- Escalabilidade
- Segurança
- Legibilidade
- Facilidade de manutenção

Além disso, o uso intensivo de testes automatizados garante maior confiabilidade e prevenção contra regressões futuras.

---

# 📬 Contato

## Marcos Firmino Rodrigues

📧 Email: marcosrodrigues.code@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/marcos-rodrigues-14391426b/?skipRedirect=true
🐙 GitHub: https://github.com/marcos22-s

---

<div align="center">

### 🚀 Projeto desenvolvido para prova DSW3 — TDD com Django

Se gostou do projeto, deixe uma estrela no repositório!

</div>
