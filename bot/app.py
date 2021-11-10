import logging
import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
logging.basicConfig(level=logging.DEBUG)
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")


@app.message("こんぺこ")
def message_peko(message, say):
    say(f"<@{message['user']}>さん、こんぺこ～")


@app.command("/hello-bolt-python-heroku")
def hello(body, ack):
    user_id = body["user_id"]
    ack(f"こんぺこ <@{user_id}>!")


from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)    

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
