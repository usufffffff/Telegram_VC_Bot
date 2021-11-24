HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech" 
from pyrogram import Client as c API_ID = input("\nEnter Your API_ID:\n > ") API_HASH = input("\nEnter Your API_HASH:\n > ") print("\n\n Enter Phone number when asked.\n\n") i = c(":memory:", api_id=API_ID, api_hash=API_HASH) with i: ss = i.export_session_string() print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n") print(f"\n{ss}\n")
