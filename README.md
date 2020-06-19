# SalC1 Discord Invite Requester

This is just a simple tool custom made for the SalC1 discord to allow a single request per IP per day to generate an invite link to prevent DM bots entering the SalC1 server.

# How to run

tested with python 3.7 and 3.8

create a `.env` file in this folder with these contents:
```
TOKEN=""
SECRET_KEY='insecure secret pelase change'
RECAPTCHA_PUBLIC_KEY="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY="6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
```

the recaptcha keys are example keys, this captcha will always go through

then, run `python -m pip install -r requirements.txt` to install all requirements

to start the server, run `python main.py`