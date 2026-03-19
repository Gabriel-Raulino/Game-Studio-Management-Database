# 🎮 Sistema de Gestão para Estúdio de Jogos

Este projeto apresenta o design e a implementação de um banco de dados relacional robusto para gerenciar as operações de um estúdio de desenvolvimento de jogos. O sistema centraliza informações críticas, desde a gestão de recursos humanos e ciclo de desenvolvimento até o desempenho comercial e relacionamento com a comunidade.

## 🚀 Diferenciais do Projeto
* **Visão 360° do Estúdio:** Integração entre Produção, Conteúdo e Comercial.
* **Inteligência Artificial:** Uso de IA Generativa (Gemini) para análise qualitativa de feedbacks de jogadores.
* **Gestão de RH:** Estrutura hierárquica para supervisão de desenvolvedores (auto-relacionamento).
* **Gamificação:** Controle de itens colecionáveis, raridade e pontuação por fases.

## 🛠️ Tecnologias Utilizadas
* **Banco de Dados:** SQL (Script DDL incluso).
* **Linguagem:** Python (Integração com Banco de Dados).
* **IA:** API do Google Gemini (Análise de sentimentos).
* **Modelagem:** brModelo v3.31.

## 📊 Modelagem de Dados

### Modelo Conceitual (DER)
O domínio do problema abrange três grandes áreas interconectadas:
1.  **Produção e RH:** Cadastro de desenvolvedores, especialidades e hierarquia de supervisão.
2.  **Desenvolvimento de Conteúdo:** Gestão de Jogos, Engines, Fases, Tarefas e Itens.
3.  **Comercial e Comunidade:** Lançamento em Plataformas/Lojas, registro de Vendas e Avaliações de jogadores.

Abaixo apresenta-se o Diagrama Entidade-Relacionamento (DER) desenvolvido utilizando a ferramenta brModelo v3.31.
<img width="1343" height="576" alt="image" src="https://github.com/user-attachments/assets/f55999c9-9c62-4283-a091-6a3620bd6f99" />

### Modelo Lógico
Derivado do modelo conceitual, definindo chaves primárias (PK), chaves estrangeiras (FK) e tipos de dados otimizados.
<img width="1453" height="852" alt="image" src="https://github.com/user-attachments/assets/c93b3cec-f85a-4675-a93d-59bb2995b84c" />

## 💻 Funcionalidades da Aplicação
A solução inclui uma aplicação em Python que realiza:
* **Operações CRUD:** Criação, leitura, atualização e deleção de registros.
* **Relatórios Gerenciais:** Geração de gráficos de desempenho comercial e de produção.
* **Análise de Feedbacks:** Integração com a IA Gemini para transformar comentários de jogadores em decisões estratégicas.

## 📂 Estrutura de Arquivos
* `Sistema de Gestão para Estúdio de Jogos (DDL).sql`: Script de criação das tabelas e integridade.
* `Projeto.py` / `Tables.py` / `Drop.py`: Código-fonte da aplicação e interface com o banco.
* `Sistema de Gestão para Estúdio de Jogos.pdf`: Documentação detalhada do projeto.
* `insercao.txt`: Dados de exemplo para teste do sistema.
* `Sistema de Gestão para Estúdio de Jogos (Modelo Conceitual).brM3` / `Sistema de Gestão para Estúdio de Jogos (Modelo Lógico).brM3`: Modelagem conceitual e lógica do banco de dados.

---
**Desenvolvido por:** Gabriel Raulino Dal Pont & Giordano da Rosa Correa.
