from dotenv import load_dotenv
from pathlib import Path
import os

home_dir = os.path.expanduser("~")
dotenv_path = Path(home_dir) / "Keys" / "OpenAIService" / ".env"
# dotenv_path = Path('libs/utils/.env') # if have .env inside project
load_dotenv(dotenv_path=dotenv_path)

default_db_type="mysql" #mysql or pg
healthcheck_interval = 1 # 1min

if default_db_type =="mysql":
    db_host_url =os.getenv('MYSQL_HOST', '')
    db_host_port = int(os.getenv('MYSQL_PORT', '3306'))
    db_host_user = os.getenv('MYSQL_USERNAME', '')
    db_host_pwd = os.getenv('MYSQL_PWD', '')
else:
    db_host_url =os.getenv('PGMYSQL_HOST', '')
    db_host_port = int(os.getenv('PGMYSQL_PORT', '5432'))
    db_host_user = os.getenv('PGMYSQL_USERNAME', '')
    db_host_pwd = os.getenv('PGMYSQL_PWD', '')
db_user = "userinfo"
db_user_apikeytable = "apikeys"
db_user_basetable='userbasicinfo'
db_log = "log_db"


apihostip = os.getenv('APISERVICE_HOST_IP', '')
apihostport = int(os.getenv('APISERVICE_HOST_PORT', '8000'))
ai_providers=["ollama","lm-studio","azure","openai"]



# LLMs
ollama_host_url = os.getenv('OLLAMA_HOST_URL', 'http://localhost')
ollama_host_port=int(os.getenv('OLLAMA_HOST_PORT', '11434'))
ollama_llm_models=os.getenv('OLLAMA_LLM_MODELS', '').split(',')
ollama_embed_models=os.getenv('OLLAMA_EMBEDDING_MODELS', '').split(',')
ollama_embed_chunksize=int(os.getenv('OLLAMA_EMBEDDING_CHUNKSIZES', '1000'))
# LM Studio
lmstudio_host_url = os.getenv('LMSTUDIO_HOST_URL', 'http://localhost:1234/v1')
lmstudio_apikey=os.getenv('LMSTUDIO_APIKEY', 'lm-studio')
lmstudio_llm_models=os.getenv('LMSTUDIO_LLM_MODELS', '').split(',')
lmstudio_embed_models=os.getenv('LMSTUDIO_EMBEDDING_MODELS', '').split(',')
lmstudio_embed_chunksize=int(os.getenv('LMSTUDIO_EMBEDDING_CHUNKSIZES', '1000'))
# Azure OpenAI Service
azure_openai_api_version = os.getenv('AZURE_OPENAI_API_VERSION', '')
azure_openai_api_type = os.getenv('AZURE_OPENAI_API_TYPE', 'azure')
azure_openai_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT', '')
azure_openai_apikey = os.getenv('AZURE_OPENAI_API_KEY', '')
azure_openai_developmentname = os.getenv('AZURE_OPENAI_DELOYMENT_NAME', '')
azure_openai_llm_models=os.getenv('AZURE_OPENAI_LLM_MODELS', '').split(',')
azure_openai_llm_modelversions=os.getenv('AZURE_OPENAI_LLM_MODELS_VERSIONS', '').split(',')
# OpenAI
openai_apikey = os.getenv('OPENAI_API_KEY', '')
openai_llm_models=os.getenv('OPENAI_LLM_MODELS', '').split(',')