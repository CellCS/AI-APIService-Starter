
from generateApiKey import generateApiKey
import json
import datetime

class ServiceValidation:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ServiceValidation, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    def __init__(self):
        self.token_history = '{ "previous":0,"usage":0,"deposit":0, "total":0, "updated":""}'
        self.validated_apikeys=[]
    def utc_now(self):
        return datetime.datetime.now(tz=datetime.timezone.utc)

    async def generate_apikey(self):
        try:
            seed='12'
            secret='Topsecrect'
            api_key=await generateApiKey(secret,seed,prefix='sk',add_dashes=True)
        except Exception as e:
            print(e)
        if api_key is None:
            api_key=""
        # sk-4e481e81-85c9-5174-b534-540a5d9208cd
        return api_key
    
    def update_apikey_token(self, apikey, token, isdeposit):
        if token < 1:
            return False
        sql_query=f"SELECT total_tokens, tokens_history FROM userinfo.apikeys WHERE  apikey = {apikey}"
        current_token = 0
        token_history= { "previous":0,"usage":0,"deposit":0, "total":0, "updated_at":""}
        token_history["previous"] = current_token
        if isdeposit is True:
            token_history["deposit"] = token
            token_history["total"] = current_token + token
        else:
            token_history["usage"] = token
            token_history["total"] = current_token - token
        token_history["updated_at"] = str(self.utc_now)
        json.dumps(token_history,ensure_ascii=False)
