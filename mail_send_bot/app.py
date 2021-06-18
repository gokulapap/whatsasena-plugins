import smtplib
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
  return "hello world"

@app.route('/sendmail', methods=["POST"])
def sender():
 if request.method == "POST":
  resp = MessagingResponse()
  body = request.form.get('Body')
  sp = body.split(';')
  if len(sp) == 1:
   resp.message("❌ *No subject and body is Given*")
   resp.message("⏩ *Syntax is : .sendmail ; subject ; body ; mail id list*")
   return str(resp)
  cmd = sp[0].strip()
  sub = sp[1].strip()
  msg = sp[2].strip()
  mails = sp[3].strip()

  mails = mails.split()

  for dest in mails:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("{your_mail_here}", "{password_here}")      # add your mail id and password
    message = "Subject: {}\n\n{}".format(sub, msg)      
    s.sendmail("{your_mail_here}", dest, message)       # add your mail id here
    resp.message('✅ *Mail sent successfully to {}*'.format(dest))
    s.quit()

 return str(resp)

if __name__ == "__main__":
  app.run(port=5000)
