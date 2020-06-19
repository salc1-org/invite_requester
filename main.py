
from flask import Flask, render_template, request, redirect, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, SubmitField

import config
import discord_on_demand_invite


app = Flask(__name__)

class ReCaptcha(FlaskForm):
    recaptcha = RecaptchaField()
    submit = SubmitField('Get Invite')

app.config.from_object(config.Config)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1 per second"]
)

@app.route("/")
def discord():
    form = ReCaptcha(request.form)
    return render_template('captcha.html', form=form)

@app.route("/getinvite", methods=['POST'])
@limiter.limit("1 per day", deduct_when=lambda response: response.status_code == 302)
def getinvite():
    form = ReCaptcha(request.form)
    if form.validate_on_submit():
        print("valid")
        return redirect("https://discord.gg/" + discord_on_demand_invite.get_invite())
    return redirect(url_for("discord"), code=303)

@app.errorhandler(429)
def rate_limit_reached(e):
    return render_template('error.html'), 404

if __name__=="__main__":
    app.run()
