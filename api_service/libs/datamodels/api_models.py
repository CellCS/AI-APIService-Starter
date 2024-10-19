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
    apiprovider: str
class ModelsResponse(BaseModel):
    models: list