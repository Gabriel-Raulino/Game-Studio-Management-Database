# 🎮 Game Studio Management System / Sistema de Gestão para Estúdio de Jogos

<details>
<summary>🇺🇸 <b>Read in English</b></summary>
<br>

This project presents the design and implementation of a robust relational database to manage the operations of a game development studio. The system centralizes critical information, ranging from human resources management and the development cycle to commercial performance and community relations.

### 🚀 Key Features
* **360° Studio View:** Integration between Production, Content, and Commercial departments.
* **Artificial Intelligence:** Use of Generative AI (Gemini) for qualitative analysis of player feedback.
* **HR Management:** Hierarchical structure for developer supervision (self-referencing relationship).
* **Gamification:** Tracking of collectible items, rarity, and scoring by stages/levels.

### 🛠️ Technologies Used
* **Database:** SQL (DDL Script included).
* **Language:** Python (Database integration).
* **AI:** Google Gemini API (Sentiment analysis).
* **Modeling:** brModelo v3.31.

### 📊 Data Modeling

#### Conceptual Model (ERD)
The problem domain covers three major interconnected areas:
1.  **Production and HR:** Registration of developers, specialties, and supervision hierarchy.
2.  **Content Development:** Management of Games, Engines, Stages, Tasks, and Items.
3.  **Commercial and Community:** Release on Platforms/Stores, Sales tracking, and Player Reviews.

Below is the Entity-Relationship Diagram (ERD) developed using the brModelo v3.31 tool.
<img width="1343" height="576" alt="image" src="https://github.com/user-attachments/assets/f55999c9-9c62-4283-a091-6a3620bd6f99" />

#### Logical Model
Derived from the conceptual model, defining primary keys (PK), foreign keys (FK), and optimized data types.
<img width="1453" height="852" alt="image" src="https://github.com/user-attachments/assets/c93b3cec-f85a-4675-a93d-59bb2995b84c" />

### 💻 Application Features
The solution includes a Python application that performs:
* **CRUD Operations:** Create, read, update, and delete records.
* **Management Reports:** Generation of commercial and production performance charts.
* **Feedback Analysis:** Integration with Gemini AI to transform player comments into strategic decisions.

### 📂 File Structure
* `Sistema de Gestão para Estúdio de Jogos (DDL).sql`: Table creation and integrity script.
* `Projeto.py` / `Tables.py` / `Drop.py`: Application source code and database interface.
* `Sistema de Gestão para Estúdio de Jogos.pdf`: Detailed project documentation.
* `insercao.txt`: Sample data for system testing.
* `Sistema de Gestão para Estúdio de Jogos (Modelo Conceitual).brM3` / `Sistema de Gestão para Estúdio de Jogos (Modelo Lógico).brM3`: Conceptual and logical database modeling.

---
**Developed by:** Gabriel Raulino Dal Pont & Giordano da Rosa Correa.

</details>

<details>
<summary>🇧🇷 <b>Ler em Português (BR)</b></summary>
<br>

Este projeto apresenta o design e a implementação de um banco de dados relacional robusto para gerenciar as operações de um estúdio de desenvolvimento de jogos. O sistema centraliza informações críticas, desde a gestão de recursos humanos e ciclo de desenvolvimento até o desempenho comercial e relacionamento com a comunidade.

### 🚀 Diferenciais do Projeto
* **Visão 360° do Estúdio:** Integração entre Produção, Conteúdo e Comercial.
* **Inteligência Artificial:** Uso de IA Generativa (Gemini) para análise qualitativa de feedbacks de jogadores.
* **Gestão de RH:** Estrutura hierárquica para supervisão de desenvolvedores (auto-relacionamento).
* **Gamificação:** Controle de itens colecionáveis, raridade e pontuação por fases.

### 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** SQL (Script DDL incluso).
* **Linguagem:** Python (Integração com Banco de Dados).
* **IA:** API do Google Gemini (Análise de sentimentos).
* **Modelagem:** brModelo v3.31.

### 📊 Modelagem de Dados

#### Modelo Conceitual (DER)
O domínio do problema abrange três grandes áreas interconectadas:
1.  **Produção e RH:** Cadastro de desenvolvedores, especialidades e hierarquia de supervisão.
2.  **Desenvolvimento de Conteúdo:** Gestão de Jogos, Engines, Fases, Tarefas e Itens.
3.  **Comercial e Comunidade:** Lançamento em Plataformas/Lojas, registro de Vendas e Avaliações de jogadores.

Abaixo apresenta-se o Diagrama Entidade-Relacionamento (DER) desenvolvido utilizando a ferramenta brModelo v3.31.
<img width="1343" height="576" alt="image" src="https://github.com/user-attachments/assets/f55999c9-9c62-4283-a091-6a3620bd6f99" />

#### Modelo Lógico
Derivado do modelo conceitual, definindo chaves primárias (PK), chaves estrangeiras (FK) e tipos de dados otimizados.
<img width="1453" height="852" alt="image" src="https://github.com/user-attachments/assets/c93b3cec-f85a-4675-a93d-59bb2995b84c" />

### 💻 Funcionalidades da Aplicação
A solução inclui uma aplicação em Python que realiza:
* **Operações CRUD:** Criação, leitura, atualização e deleção de registros.
* **Relatórios Gerenciais:** Geração de gráficos de desempenho comercial e de produção.
* **Análise de Feedbacks:** Integração com a IA Gemini para transformar comentários de jogadores em decisões estratégicas.

### 📂 Estrutura de Arquivos
* `Sistema de Gestão para Estúdio de Jogos (DDL).sql`: Script de criação das tabelas e integridade.
* `Projeto.py` / `Tables.py` / `Drop.py`: Código-fonte da aplicação e interface com o banco.
* `Sistema de Gestão para Estúdio de Jogos.pdf`: Documentação detalhada do projeto.
* `insercao.txt`: Dados de exemplo para teste do sistema.
* `Sistema de Gestão para Estúdio de Jogos (Modelo Conceitual).brM3` / `Sistema de Gestão para Estúdio de Jogos (Modelo Lógico).brM3`: Modelagem conceitual e lógica do banco de dados.

---
**Desenvolvido por:** Gabriel Raulino Dal Pont & Giordano da Rosa Correa.

</details>
