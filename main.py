from auth import AuthorizationValidation
from oncall import OnCall 

def checkAuth():
    auth = AuthorizationValidation()
    auth.validate_auth()

if __name__ == "__main__":
    checkAuth()
    oncall = OnCall()
    oncall.whos_on_call()
