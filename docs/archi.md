# Architecture

## Classes Schema

### API Service

```mermaid
classDiagram
      APIService o--  UserDatabase
      APIService o--  LLMService
      APIService o--  LogDatabase
      
      class APIService{
          + Auth
          ...
      }

      class UserDatabase{
          + MySQL
      }
      class LLMService{
          + Ollama
          + LM_Studio
          + OpenAI
          + AzureOpenAI
      }
      class LogDatabase{
          + MySQL
          ...
      }

```

### Others

## Class Details

| Classes        | File Name          | Details |
| ------------- |:-------------:| :--------:|
| APIService | [apiservice.md](./classes/apiservice.md)  | APIService|
