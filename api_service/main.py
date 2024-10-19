from fastapi import FastAPI, Depends,BackgroundTasks,Header, HTTPException
from fastapi import Depends, FastAPI, HTTPException, status, Query
from fastapi.security import HTTPBasic
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.security import APIKeyHeader
import asyncio
import pprint

from contextlib import asynccontextmanager
from pydantic import BaseModel

from libs.datamodels import api_models as apimodels
from libs.utils import app_consts as appconsts
from libs import appservice as appserv
from libs.utils import validations as validator


import uvicorn

origins = ['*']

# need rename based on your bussiness logic
appservice = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global appservice
    pprint.pprint("Starting up the application...")
    if appservice is None:
        pprint.pprint("init oneserviceobj")
        appservice = appserv.APPService()
        asyncio.create_task(run_health_check()) # start run_health_check in the background
    yield
    print("Shutting down the application...")

app = FastAPI(
    title="AI Service: AI API Service",
    description="Provide FastAPI for your AI",
    summary="",
    version="0.0.1",
    lifespan=lifespan,
    openapi_tags=apimodels.tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
security = HTTPBasic()
api_key_header = APIKeyHeader(name="APIKEY")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key not in appservice.validated_apikeys:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

################### business logic##############################################
appvalidator = validator.ServiceValidation()

async def run_health_check():
    try:
        while True:
            pprint.pprint("Running health check, do something")
            await asyncio.sleep(appconsts.healthcheck_interval * 60)
            appservice.set_validated_apikey()
    except Exception as e:
        pprint.pprint(f"Health check failed: {e}")

################### business logic##############################################
@app.get("/hit_test")
async def hit_test(isauth: str = Depends(verify_api_key)):
    return {"Happy": "Coding"}

@app.get("/self_validation")
async def hit_test(isauth: str = Depends(verify_api_key)):
    await appvalidator.generate_apikey()
    return {"Happy": "Coding"}

@app.post("/models", response_model=apimodels.ModelsResponse, tags=["Chatbot_Service"],responses={200: {"description": "A successful response", "content": {"application/json": {"example": {"models": ["gpt-4o, gpt-4omini"]}}}}})
async def model(payloaddata: apimodels.ModelsPayload, isauth: str = Depends(verify_api_key)):
    """
    Get available models by a specific provider like Ollama, LM Studio, Azure OpenAI or OpenAI. 
    - **Message**: LLM model names.
    """
    res = appservice.getmodels(payloaddata.apiprovider)
    if len(res) > 0:
        return {"models": res}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect parameter",
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host=appconsts.apihostip, port = appconsts.apihostport, reload=False)