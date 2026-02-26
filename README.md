# 📦 Backup de Arquivos em Python

Este projeto é uma aplicação simples em **Python** para realizar **backup de arquivos** de uma pasta de origem para uma pasta de destino no sistema operacional Windows.

O script copia apenas **arquivos** (não copia pastas) e exibe um **resumo final** com a quantidade de arquivos copiados e ignorados, além de registrar erros usando um sistema de **log**.

---

## 🚀 Funcionalidades

- ✅ Verifica se a pasta de origem existe  
- 📁 Cria automaticamente a pasta de destino, se necessário  
- 📄 Copia arquivos preservando metadados (data, permissões, etc.)  
- 🚫 Ignora diretórios  
- 📊 Exibe resumo do backup ao final  
- 📝 Registra erros em log  

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Bibliotecas padrão:
  - `os`
  - `shutil`
  - `datetime`
- Logger customizado (`log.py`)

---

## 📂 Estrutura do Projeto

```text
📁 projeto-backup
│
├── backup.py          # Script principal
├── log.py             # Configuração do logger
└── README.md          # Documentação
```

---

## ⚙️ Configuração

No início do script, ajuste os caminhos das pastas conforme sua necessidade:

```python
PASTA_ORIGEM = r'C:\Users\user\Documents\Origem'
PASTA_DESTINO = r'C:\Users\user\Documents\Destino'
```

> ⚠️ **Atenção:**  
> - A pasta de origem **precisa existir**  
> - A pasta de destino será criada automaticamente, se não existir  

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado  
2. Abra o terminal na pasta do projeto  
3. Execute o comando:

```bash
python backup.py
```

---

## 📋 Exemplo de Saída no Terminal

```text
[INÍCIO] Iniciando o processo de backup...

[INFO] Arquivo copiado: C:\Origem\arquivo1.txt
[INFO] Ignorando pasta_exemplo (não é arquivo)

[INFO] Resumo do Backup - 2026-02-26 19:45:10

Arquivos copiados: 1
Arquivos ignorados: 1
```

---

## 🧠 Como Funciona

1. Valida a existência da pasta de origem  
2. Cria a pasta de destino, se necessário  
3. Percorre os arquivos da pasta de origem  
4. Copia apenas arquivos  
5. Exibe um resumo ao final do processo  
6. Registra erros no log, se ocorrerem  

---

## 🛡️ Tratamento de Erros

- Erros durante a cópia de arquivos são capturados  
- O script não interrompe o processo por falhas individuais  
- Erros críticos são registrados usando o logger  

---

## 📌 Melhorias Futuras (Sugestões)

- 🔁 Backup incremental  
- 📁 Opção para copiar subpastas  
- ⚙️ Configuração via arquivo `.env` ou `.json`  
- 🕒 Agendamento automático (Task Scheduler)  

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e pessoais.

---

👨‍💻 Desenvolvido com Python para automatizar tarefas simples de backup.
