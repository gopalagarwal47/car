import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MAIL_ID="agarwalgopal47@gmail.com "
PASS="hxedysoeoypjeysc "

def message_mail(name, phone, address, textarea):
	s = smtplib.SMTP('smtp.gmail.com', 587)  
	s.starttls() 
	
	s.login(MAIL_ID, PASS) 
	
	body  = name + " wrote to you :" + phone + address + textarea  + "\n. His email is: " 
	# message to be sent 

	message = MIMEMultipart()

	message['Subject'] = "Somebody send you a new message!"
	message["From"] = MAIL_ID
	message["To"] = "agarwalgopal47@gmail.com"
	message.attach(MIMEText(body, 'plain'))

	s.sendmail(MAIL_ID, "agarwalgopal47@gmail.com", message.as_string())

	# terminating the session 
	s.quit() 






# def message_mail(name, phone, address, textarea):
#      s = smtplib.SMTP('smtp.gmail.com', 587)
#      s.starttls()
#      body = name + " wrote to you :" + textarea + phone + address +" \n. His email is: "
#      # message to be sent
#      message = MIMEMultipart()
#      message['Subject'] = "Somebody send you a new message!"
#      message["To"] = "agarwalgopal47@gmail.com"
#      message.attach(MIMEText(body, 'plain'))
#      s.sendmail(msg,"agarwalgopal47@gmail.com",message.as_string())

#      # terminating the session
#      s.quit()
