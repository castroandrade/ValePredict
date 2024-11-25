# **ValePredict**

Projeto para previsão de lucro e custos associados ao plantio de diferentes culturas agrícolas, desenvolvido utilizando Django.

---

## **Índice**
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Requisitos de Instalação](#requisitos-de-instalação)
5. [Como Executar o Projeto](#como-executar-o-projeto)

---

## **Descrição do Projeto**

O **ValePredict** é uma aplicação web que auxilia produtores agrícolas na tomada de decisão ao prever os custos, receitas e lucros associados ao plantio de diferentes culturas. O sistema utiliza dados fornecidos pelos usuários, como área disponível e área plantada, para realizar os cálculos.

A aplicação também conta com um sistema de autenticação de usuários e interface amigável para visualização dos resultados.

---

## **Funcionalidades**

- **Página de Previsão:**
  - Entrada de dados como cultura, área disponível e área plantada.
  - Cálculo de custos, receitas, lucros e prejuízos estimados.
- **Página de Resultados:**
  - Exibição detalhada das informações inseridas e dos resultados previstos.
- **Sistema de Autenticação:**
  - Login e cadastro de usuários.
- **Interface Responsiva:**
  - Design otimizado para uso em dispositivos móveis e desktops.

---

## **Tecnologias Utilizadas**

- **Backend:**
  - [Django](https://www.djangoproject.com/)
- **Frontend:**
  - HTML5
  - CSS3 (com design responsivo e estilos personalizados)
- **Banco de Dados:**
  - SQLite (para desenvolvimento)
- **Outras Tecnologias:**
  - Bootstrap (opcional para estilização)
  - Django Forms para validação de entrada

---

## **Requisitos de Instalação**

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.10+
- Pip (gerenciador de pacotes Python)
- Virtualenv (opcional, mas recomendado)

---

## **Como Executar o Projeto**

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/valepredict.git
   cd valepredict


2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt

4. **Realizar a migração do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver

6. **Acesse o sistema:**
   ```bash
   Abra o navegador e acesse http://127.0.0.1:8000.

