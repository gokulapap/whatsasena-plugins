from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from googlesearch import search


app = Flask(__name__)

@app.route("/pdf", methods=["GET", "POST"])
def reply_whatsapp():
    response = MessagingResponse()
    body = request.form.get('Body')
    query = body.split(';')[1]
    query = query + ' filetype:pdf'
    pdfs = []
    msg = response.message("Fetching Best pdfs for {} ...".format(body.split(';')[1]))

    for j in search(query, tld="com", num=5, stop=7, pause=1):
        if j[-1:-5:-1] == 'fdp.':
          pdfs.append(j)

    for i in pdfs:
      m = response.message("pdf")
      m.media(i)
    return str(response)

if __name__ == "__main__":
    app.run()
