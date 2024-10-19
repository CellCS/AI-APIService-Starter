# Architecture

## Classes Schema

### API Service

```mermaid
classDiagram
      APIService o--  Datamodels
      APIService o--  APPService

      APPService o--  UserDB
      APPService o--  LogDB
      APPService o--  LLMService
      APPService o--  AIAgentService
      APPService o--  EmbeddingService
      
      class APIService{
          + Endpoints
          ...
      }
      class Datamodels{
          + Category
          + Payload
          + Response
          ...
      }
      
      class APPService{
          + Auth
          ...
      }

      class UserDB{
          + MySQL
          + userinfo
          + apikeys
      }
      class LogDB{
          + MySQL
          + loginfo
      }

      class LLMService{
          + Ollama
          + LM_Studio
          + OpenAI
          + AzureOpenAI
      }

      class AIAgentService {
          + AutoGen
          + LangChain
      }

      class EmbeddingService {
          + Ongoing...
      }

```

### Others

## Class Details

| Classes        | File Name          | Details |
| ------------- |:-------------:| :--------:|
| APIService | [apiservice.md](./classes/apiservice.md)  | APIService|
