from flask import Flask, request
import telebot
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
bot = telebot.TeleBot("xxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxx")    # add telebot api key

resp = MessagingResponse()

@app.route('/')
def home():
 return "app is working"

@app.route("/telepost", methods=["POST"])
def telpost():
 msg = request.form.get('Body')
 msg = msg.split(';')
 msg = msg[1]
 bot.send_message({YOUR_TELEGRAM_CHAT_ID}, msg)              # add your telegram chat id here
 resp.message("✅ *Sucessfully sent the message to telegram*")
 return str(msg)

if __name__ == "__main__":
 app.run(port=5000)
