from pydantic import BaseModel

tags_metadata = [
    {
        "name": "Authorize",
        "description": "Operations related to Authorize management."
    },
    {
        "name": "Chatbot_Service",
        "description": "Operations related to Chatbot."
    }
]

class ConnectionTestResponse(BaseModel):
    Message: str

class AuthResponse(BaseModel):
    message: str
    user: str


class ModelsPayload(BaseModel):
    llmclient: str
class ModelsResponse(BaseModel):
    models: list

class ChatPayload(BaseModel):
    llmclient: str
    model:str
    messages:list
class ChatResponse(BaseModel):
    client: str
    model: str
    messages: list
    status_code: int
    details: str
    response: dict

class GeneratePayload(BaseModel):
    llmclient: str
    model:str
    prompt:str
    messages:dict
class GenerateResponse(BaseModel):
    client: str
    model: str
    messages: list
    status_code: int
    details: str
    response:dict

class V1ChatCompletionsPayload(BaseModel):
    llmclient: str
    model:str
    messages:dict
class V1ChatCompletionsResponse(BaseModel):
    client: str
    model: str
    messages: list
    status_code: int
    details: str
    response:dict