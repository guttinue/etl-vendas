# 🚀 Desafio Técnico - ETL de Vendas

## 🔹 Visão Geral
Este projeto tem como objetivo a criação de um pipeline ETL para processar dados de vendas, agregá-los e gerar insights.

## 🔹 O que foi feito:
✅ Extração e tratamento dos dados de vendas.  
✅ Criação do arquivo CSV unificado com dados prontos para análise.  
✅ Organização do repositório e código para fácil execução.  

## 🔹 O que faltou:
❌ Implementação da carga no MySQL (Cloud SQL).  
❌ Construção do dashboard no Power BI.  

## 🔹 Como Rodar a Extração e Tratamento:
1. Instale as bibliotecas necessárias:
    ```sh
    pip install pandas
    ```
2. Rode o script para extração e tratamento:
    ```sh
    python src/extracao_tratamento.py
    ```
3. O arquivo final gerado estará em `data/vendas_unificadas.csv`.

## 🔹 Próximos Passos (Se Tivesse Mais Tempo)
Se eu tivesse mais tempo, seguiria com:
1️⃣ Criar a conexão com MySQL e fazer a carga dos dados.  
2️⃣ Construir as tabelas `vendas`, `vendas_por_estado` e `vendas_por_categoria`.  
3️⃣ Criar o dashboard no Power BI para visualização dos dados.  

## 🔹 Conclusão
Infelizmente, não consegui finalizar a carga no banco de dados dentro do prazo, mas estruturei a parte de **extração e tratamento** corretamente, e o pipeline está pronto para continuar a partir da carga no banco.

