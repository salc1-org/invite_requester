from dotenv import load_dotenv
import os
load_dotenv()


class Config():
    SECRET_KEY = os.environ["SECRET_KEY"]
    RECAPTCHA_PUBLIC_KEY = os.environ["RECAPTCHA_PUBLIC_KEY"]
    RECAPTCHA_PRIVATE_KEY = os.environ["RECAPTCHA_PRIVATE_KEY"]
    RECAPTCHA_DATA_ATTRS = {"theme": "dark"}