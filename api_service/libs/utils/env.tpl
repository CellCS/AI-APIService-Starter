
SERVER_DEPLOY_MODE="dev"#"dev" and "prod"

APISERVICE_HOST_IP="0.0.0.0"
APISERVICE_HOST_PORT='8000'

EMBEDDING_MODELS_OVERLAP=100
EMBEDDING_CHUNKSIZES="1000,1536"
###############################  Ollama  #############################
OLLAMA_HOST_URL="http://localhost"
OLLAMA_HOST_PORT=11434
OLLAMA_LLM_MODELS="llama3.2,llama3.1"
OLLAMA_EMBEDDING_MODELS="nomic-embed-text,"
OLLAMA_EMBEDDING_CHUNKSIZES="1000"

###############################  LM Studio  #############################
LMSTUDIO_HOST_URL="http://localhost:1234/v1"
LMSTUDIO_APIKEY="lm-studio"
LMSTUDIO_LLM_MODELS="llama3.2,llama3.1"
LMSTUDIO_EMBEDDING_MODELS="nomic-embed-text,"
LMSTUDIO_EMBEDDING_CHUNKSIZES="1000"

###############################  AZURE_OPENAI_SERVICE  #############################
AZURE_OPENAI_API_VERSION=""
AZURE_OPENAI_API_TYPE="azure"
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_DELOYMENT_NAME=""
AZURE_OPENAI_LLM_MODELS="gpt-4o-mini,gpt-4o"
AZURE_OPENAI_LLM_MODELS_VERSIONS="2023-03-15-preview,2023-03-15-preview"
AZURE_OPENAI_EMBEDDING_MODELS="text-embedding-3-small,text-embedding-3-large"
AZURE_OPENAI_EMBEDDING_MODELS_CHUNKSIZES="1536"

###############################  OPENAI_API  #############################
OPENAI_API_KEY=""
OPENAI_LLM_MODELS="gpt-4o-mini,gpt-4o"
OPENAI_EMBEDDING_MODELS="text-embedding-3-small,text-embedding-3-large"
OPENAI_EMBEDDING_MODELS_CHUNKSIZES="1536"

############################## API Service Database#############################
# MYSQL Server
MYSQL_HOST="127.0.0.1"
MYSQL_PORT="3306"
MYSQL_USERNAME="root"
MYSQL_PWD="root"
MYSQL_DRIVER="mysqlconnector"

# pg Server
PGMYSQL_HOST="127.0.0.1"
PGMYSQL_PORT="3306"
PGMYSQL_USERNAME="root"
PGMYSQL_PWD="root"
PYMYSQL_DRIVER="pymysql"
###############################END#############################

