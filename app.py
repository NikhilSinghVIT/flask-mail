from flask import Flask 
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'youremail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_DEFAULT_SENDER'] = 'youremail@gmail.com'
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)
@app.route('/')
def index():
    msg = Message('Hey There', recipients=['recieveremail@gmail.com'])
    msg.html = '<b>This is a test mail,please do not reply.</b>'
    mail.send(msg)

    return 'Message has been sent!'

@app.route('/bulk')
def bulk():
	#the reciever's email can be in a dictionary as given below or in a list
	users = [{'name':'a','email':'example1@gmail.com'},{'name':'b','email':'example2@gmail.com'},{'name':'c','email':'example3@gmail.com'}]

	with mail.connect() as conn:
		for user in users:
			msg = Message('Bulk',recipients=[user['email']])
			msg.body = 'It is a test email ,please dont reply'
			conn.send(msg)
	return 'mail sent'


if __name__ == '__main__':
    app.run()