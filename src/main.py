import os
from dotenv import load_dotenv
from oncall import OnCall 
from slack_bolt import App
from auth import AuthorizationValidation
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

def checkAuth():
    auth = AuthorizationValidation()
    auth.validate_auth()

app = App(token=os.getenv("SLACK_BOT_TOKEN"))

@app.message("whosoncall")
def show_current_oc(ack, say): 
    oncall = OnCall()

    ack()
    say(f"Current on call user is: {oncall.whos_on_call()}")

if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
