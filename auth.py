from base import DDClient
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.exceptions import ApiException
from datadog_api_client.v1.api.authentication_api import AuthenticationApi 

class AuthorizationValidation(DDClient):
    def __init__(self):
        super().__init__()
        
    def validate_auth(self):
        configuration = Configuration()
        try:
            with ApiClient(configuration) as api_client:
                api_instance = AuthenticationApi(api_client)
                response = api_instance.validate()

                print(response)
        except ApiException as e:
            print(f"exception happened with the API: {e}"  )
