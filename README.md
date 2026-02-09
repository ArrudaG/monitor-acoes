# 📊 Market Monitor — Stocks Alert System

Aplicação em Python para monitoramento automatizado de preços de ativos financeiros com envio de alertas por email quando condições configuradas são atingidas.

O objetivo do projeto é demonstrar habilidades em **automação, integração com APIs, execução em nuvem e organização de código Python**.

---

## 🚀 Funcionalidades

- Monitoramento de ações
- Envio automático de alertas por email
- Persistência de estado para evitar alertas duplicados
- Sistema de logging
- Execução automatizada via GitHub Actions
- Execução local para desenvolvimento e testes

---

## 🧱 Estrutura do projeto

```text
.
├── .github/workflows/
│   └── monitor.yml
├── src/
│   ├── config/
│   ├── infra/
│   ├── logs/        # utilizado apenas para execução local
│   ├── services/
│   ├── estado.json
│   └── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Tecnologias

- Python
- GitHub Actions
- SMTP (envio de email)
- dotenv
- logging

---

## ☁️ Execução automatizada

O monitor roda automaticamente via GitHub Actions usando agendamento cron:

```yaml
*/15 * * * *
```

Isso permite a execução do sistema na nuvem sem necessidade de servidor dedicado.

---

## ▶️ Executar localmente

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar o monitor:

```bash
python src/main.py
```

---

## 📚 Aprendizados

Este projeto envolveu:

- Estruturação de projetos Python
- Automação com GitHub Actions
- Consumo de APIs
- Persistência de estado
- Logging de aplicações
- Integração com serviços de email
- Deploy de scripts de automação
****
