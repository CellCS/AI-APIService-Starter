# AI-APIService-Starter

Deploy AI Services with a REST API: Combining Local LLMs (Ollama, LM Studio) and OpenAI in FastAPI

## Start with local host

under AI-APIService-Starter/

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
pip3 install -r api_service/requirements.txt
```

then under: AI-APIService-Starter/api_service

```bash
python3 main.py
```

```bash
http://127.0.0.1:8000/docs#/
```

```bash
curl http://localhost:8000
```

Testing: 

```bash
curl -H "APIKEY: user_api_key" http://127.0.0.1:8000/hit_test
```

```bash
curl -H "APIKEY: api_key1" http://127.0.0.1:8000/hit_test
```

```bash
curl -X POST http://127.0.0.1:8000/models \
  -H "Content-Type: application/json" \
  -H "Connection: close" \
  -H "APIKEY: api_key1" \
  -d '{"llmclient": "ollama"}'
```

```bash
curl -L \
    -H "Accept: application/json" \
    -H "Connection: close" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "ollama"}' \
    http://127.0.0.1:8000/models --verbose
```

### Ollama

chat:

```bash
curl -L \
    -H "Accept: application/json" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "ollama", "model": "llama3.2", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}' \
    http://127.0.0.1:8000/chat --verbose
```

generate:

```bash
curl -L \
    -H "Accept: application/json" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "ollama", "model": "llama3.2", "prompt", "What color is the sky at different times of the day? Respond using JSON", "messages": [{"format": "json", "stream": false}]}' \
    http://127.0.0.1:8000/generate --verbose
```

### LM Studio

```bash
curl -L \
    -H "Accept: application/json" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "lm-studio", "model": "llama3.2", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}' \
    http://127.0.0.1:8000/chat --verbose
```

### OpenAI

```bash
curl -L \
    -H "Accept: application/json" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "openai", "model": "gpt-4o", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}' \
    http://127.0.0.1:8000/chat
```

### AzureOpenAI

```bash
curl -L \
    -H "Accept: application/json" \
    -H "APIKEY: api_key1" \
    -H "Content-type: application/json" \
    -d '{"llmclient": "azure", "model": "gpt-4o", "messages": [{"role": "user", "content": "Why is the sky blue?"}]}' \
    http://127.0.0.1:8000/chat
```

## API Service database (MySQL)

```bash
docker compose -f docker-compose-db.yml up -d
```

For MySQL as example:

```bash
CREATE TABLE userinfo.userbasicinfo (
    userid INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    useremail VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    signup_time DATETIME,
    last_login_time DATETIME,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

```bash
CREATE TABLE userinfo.apikeys (
    userid INT,
    apikey VARCHAR(50) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    expired_at TIMESTAMP,
    tokens_left INT DEFAULT 0,
    tokens_history TEXT
);
```

```bash
docker compose -f docker-compose-db.yml down
```
