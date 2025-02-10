# SQS API

Este projeto é uma API construída com FastAPI que publica mensagens em uma fila do Amazon SQS. A API permite enviar mensagens via um endpoint HTTP e utiliza Docker para facilitar a implantação.

![Arquitetura da aplicação](/img/arch_img.jpg)

## 📌 Tecnologias Utilizadas
- **FastAPI**
- **Boto3 (AWS SDK para Python)**
- **Docker & Docker Compose**
- **Amazon SQS**

## 🚀 Configuração e Execução

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/TechChallengeFiap-7SOT/sqs-api.git
cd sqs-api
```

### 2️⃣ Criar um Arquivo de Credenciais
Preencha o docker-compose com suas credenciais da AWS Academy

### 3️⃣ Executar com Docker

#### 🔹 Construir e subir os containers
```bash
docker-compose up --build
```

#### 🔹 A API estará disponível em:
```
http://localhost:8000
```

### 4️⃣ Testando a API

Você pode enviar uma mensagem para o SQS usando `curl`:
```bash
curl -X 'POST' 'http://127.0.0.1:8000/send-message/' \
     -H 'Content-Type: application/json' \
     -d '{"message": {"chave": "valor"}}'
```

Ou via Swagger UI:
```
http://localhost:8000/docs
```

## 📜 Licença
Este projeto é open-source e segue a licença [MIT](https://choosealicense.com/licenses/mit/).

