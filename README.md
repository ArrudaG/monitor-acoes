# Monitor de Ações do Mercado Financeiro — Sistema de Alerta de Ações

Aplicação em Python para monitoramento automatizado de preços de ativos financeiros consumindo a API da **brapi.dev**, com persistência em banco de dados `PostgreSQL` via **SQLAlchemy** e envio de alertas por email quando gatilhos de preços especificados são atingidos.

O objetivo do projeto é demonstrar habilidades em **automação, consumo de APIs REST, ORM/Modelagem de Dados e organização de código Python**.

---

## Funcionalidades

- **Consulta de cotações em tempo real:** Consumo da API da `brapi.dev` com controle de timeouts e tratamento de exceções.
- **Atualização em lote e cotações diárias:** Atualização periódica dos preços e variações percentuais dos ativos cadastrados no banco.
- **Sistema de Alertas/Gatilhos:** Identificação de notificações pendentes para gatilhos do tipo `ABOVE` (preço maior ou igual ao alvo) e `BELOW` (preço menor ou igual ao alvo).
- **Envio automático de emails:** Notificações via SMTP seguro (`smtplib` + SSL) para os gatilhos disparados.
- **Controle de notificações:** Marcação no banco de dados (`ja_notificou = True`) para evitar o envio de alertas duplicados.
- **Suíte de Testes:** Testes unitários e de integração utilizando `pytest`.

---

## Estrutura do projeto

```text
.
├── src/
│   ├── config/          
│   ├── infra/           
│   ├── models/          
│   └── services/        
├── tests/               
├── main.py              
├── README.md
└── requirements.txt
```
---



## Tecnologias



- **Linguagem: Python 3.11**

- **Banco de dados & ORM: PostgreSQL + SQLAlchemy**

- **Integração com APIs: Requests (API `brapi.dev`)**

- **Comunicação: SMTP/SSL (`smtplib`)**

- **Teste Qualidade: Pytest**



---



## Execução automatizada



O monitor roda automaticamente via GitHub Actions usando agendamento cron:



```yaml

* /15 * * * *

```



Isso permite a execução do sistema na nuvem sem necessidade de servidor dedicado.



---



## Executar localmente



Instalar dependências:



```bash

pip install -r requirements.txt

```



## Variáveis de Ambiente
 
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
 
```env
BRAPI_API_KEY=sua_chave_brapi
DATABASE_URL=sua_string_de_conexao_do_banco
EMAIL_USER=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app_do_gmail
EMAIL_TO=email_destinatario@gmail.com
```



Executar o monitor:



```bash

python main.py

```



---



## Aprendizados



Este projeto envolveu:



- Arquitetura de software em camadas e separação de responsabilidades (Services, Models, Infraestrutura).

- Mapeamento Objeto-Relacional (ORM) com SQLAlchemy.

- Integração e tratamento robusto de erros ao consumir APIs externas.

- Autenticação e envio seguro de e-mails via SSL com Python

- Cobertura de testes unitários e de integração para validar regras de negócio

**** 

