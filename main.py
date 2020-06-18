from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
import os
import discord_on_demand_invite
load_dotenv()

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1 per day"]
)

@app.route("/getinvite")
@limiter.limit("1 per day")
def getinvite():
    return discord_on_demand_invite.get_invite()

if __name__=="__main__":
    app.run()