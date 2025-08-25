# Aula de SQL

Este repositório contém uma série de exercícios de SQL projetados para ensinar modelagem de banco de dados, criação de tabelas e escrita de consultas. Os exercícios estão estruturados como handouts, e você é incentivado a completá-los na sequência.

## Começando

### 1. Dê uma estrela e faça um fork do repositório

Para acompanhar seu progresso e ter sua própria cópia do repositório:

1. **Dê uma estrela** neste repositório (Star).
2. **Faça um fork** do repositório para sua conta no GitHub. Isso criará uma cópia do repositório na sua conta.

### 2. Clone o seu fork

Após fazer o fork, clone o repositório para sua máquina local:

```bash
git clone https://github.com/<seu-usuario>/sql-lesson.git
cd sql-lesson
```

Substitua `<seu-usuario>` pelo nome do seu usuário no GitHub.

### 3. Configure o ambiente

Este projeto utiliza Python e SQLite. Siga os passos abaixo para configurar o ambiente:

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   ```
2. Ative o ambiente virtual:
   - No Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Execute os exercícios

Os exercícios estão localizados na pasta `exercises` e organizados como notebooks Jupyter. Complete-os na seguinte ordem:

1. **Exercício 01: Modelagem de Banco de Dados**
   - Abra o notebook:
     ```bash
     exercises/01_modelagem.ipynb
     ```
   - Siga as instruções no notebook para criar tabelas e inserir dados.

2. **Exercício 02: Consultas SELECT**
   - Abra o notebook:
     ```bash
     exercises/02_select.ipynb
     ```
   - Este exercício focará em escrever consultas básicas com SELECT.

3. **Exercício 03: Agregações e Agrupamentos**
   - Abra o notebook:
     ```bash
     exercises/03_dml.ipynb
     ```
   - Este exercício abordará funções de agregação e agrupamento de dados.

4. **Exercício 04: Operações JOIN**
   - Abra o notebook:
     ```bash
     exercises/04_join.ipynb
     ```
   - Pratique a escrita de consultas JOIN para combinar dados de várias tabelas.

### Observações

- Os exercícios foram projetados para serem completados em sequência. Certifique-se de finalizar um antes de passar para o próximo.
- O repositório inclui testes automatizados para validar suas soluções. Siga as instruções em cada notebook para executar os testes.

### Passo Final

Após completar os exercícios, o seu repositório forkado conterá suas soluções. Isso permitirá que você mantenha um registro do seu progresso e revise o material sempre que necessário.

Obrigado por utilizar este repositório para aprender SQL. Bons estudos!