import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = "Varsha"
email['to'] = 'varshabiswal77@gmail.com'
email['subject'] = 'Greetings!'
email.set_content(html.substitute({'name' : 'Mr.Anderson'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('varshabiswal07@gmail.com', 'piyqswrlhzynkhtv')
	smtp.send_message(email)

	print("Successfully Sent!")
