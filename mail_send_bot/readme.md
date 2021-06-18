# Email sender plugin
This plugin is used to send mails from whatsapp 

# deploy

* First go to https://www.twilio.com/console/sms/whatsapp/sandbox and create account and follow the steps to configure whatsapp sandbox
* Then deploy this mail_send_bot flask application to heroku and copy the url
* Then go to twilio setting and add the copied heroku url in post request 
* Whenever we send a message , twilio redirects that to our flask app
* The flask app processes and returns output


