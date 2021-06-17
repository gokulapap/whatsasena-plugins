import email
import time
import imaplib
import traceback 
from flask import Flask

app = Flask(__name__)

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "apgokul008" + ORG_EMAIL
FROM_PWD = "gokul!!8"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

@app.route('/')
def home():
 return "<h1>App is working</h1>"

@app.route('/readmail')
def read_email_from_gmail():
    result = ''
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[10])

        print("="*50, '\n')
        result = result + "---------    *Inbox of {}*    ---------\n\n".format(FROM_EMAIL)
        result = result + "="*52
        result = result + "\n\n"
        for i in range(latest_email_id, first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    result = result + 'From : ' + email_from + '\n'
                    result = result + 'Subject : ' + email_subject + '\n\n'
                    result = result + "="*52
                    result = result + "\n\n"
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    print("="*52)
    except Exception as e:
        traceback.print_exc() 
        print(str(e))

    return result


if __name__ == "__main__":
  app.run(port=5000)

