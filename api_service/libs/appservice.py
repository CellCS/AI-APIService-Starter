from libs.datamodels import api_models as apimodels
from libs.utils import app_consts as appconsts
from libs.utils import validations as validator
from libs.db_services import lib_sql as  sqllib
import pprint

class APPService:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(APPService, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    def __init__(self):
        appvalidator = validator.ServiceValidation()
        # use mysql as default.
        appsqldb_userdb = sqllib.DatabaseConnection("mysql", appconsts.db_host_url, appconsts.db_user, appconsts.db_host_user,  appconsts.db_host_pwd, appconsts.db_host_port)
        appsqldb_logdb = sqllib.DatabaseConnection("mysql", appconsts.db_host_url, appconsts.db_log, appconsts.db_host_user,  appconsts.db_host_pwd, appconsts.db_host_port)
        self.set_validated_apikey()
    
    def set_validated_apikey(self):
        #sync from local userinfo db
        pprint.pprint("sync: set_validated_apikey")
        self.validated_apikeys = ["api_key1", "api_key2", "api_key3"]
    
    def getmodels(self, providerlabel):
        if providerlabel.lower() not in [provider.lower() for provider in appconsts.ai_providers]:
            return []
        else:
            if providerlabel == appconsts.ai_providers[0]:
                return appconsts.ollama_llm_models
            elif providerlabel == appconsts.ai_providers[1]:
                return appconsts.lmstudio_llm_models
            elif providerlabel == appconsts.ai_providers[2]:
                return appconsts.azure_openai_llm_models
            else:
                return appconsts.openai_llm_models

