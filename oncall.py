import os
from base import DDClient
from dotenv import load_dotenv
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.exceptions import ApiException
from datadog_api_client.v2.api.on_call_api import OnCallApi 

class OnCall(DDClient):
    def __init__(self):
        super().__init__()

    def whos_on_call(self):
        load_dotenv()

        ROUTING_RULES_DATA_ID = os.getenv("ROUTING_RULES_DATA_ID")
        configuration = Configuration()

        try:
            with ApiClient(configuration) as api_client:
                api_instance = OnCallApi(api_client)
                response = api_instance.get_team_on_call_users(
                    include = "responders",
                    team_id = ROUTING_RULES_DATA_ID,
                )
                print(response)
        except ApiException as e:
            raise e
