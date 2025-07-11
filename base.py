import os
from dotenv import load_dotenv
from datadog_api_client import Configuration
# from datadog_api_client.v2.api_on_call_api import OnCallApi

class DDClient:
    def __init__(self):
        load_dotenv()
        self.configuration = Configuration()
        self.configuration.enable_retry = False
        self.configuration.server_variables["site"] = os.getenv(
                "DD_SITE", "us5.datadoghq.com"
        )


