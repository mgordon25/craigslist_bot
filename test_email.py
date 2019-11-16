import smtplib
import getpass
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



sender_email = 'mgdevtest@gmail.com'
receiver_email = 'mgordon25@gmail.com'
gmail_password = 'fvfu3533'



#try:
#    gmail_password = input("Password: ")
    
#except:
#    print("error")

#TODO -- better method of password input and masking
#TODO -- add html

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

#sent_from = gmail_user
#to = ['mgordon25@gmail.com']
#subject = 'Daily report'
#body = 'Here is the daily report'

email_text = """\
From: 
To: 
Subject: 


""" #%(sent_from, ", ".join(to), subject, body)

html = """\

<a href="https://sfbay.craigslist.org/pen/apa/d/belmont-unbeatable-value-for-top-floor/7021410954.html">Real Python</a> 

"""
# -- TODO: Insert text into hyperlink

# convert to plain/html MIMEText objects
part1 = MIMEText(email_text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain text to MIMEMultipart message
# the email client will try to render the last part first

message.attach(part1)
message.attach(part2)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, gmail_password)
    server.sendmail(sender_email, receiver_email , message.as_string())
    server.close()
    

    print('Email sent')

except:
    print('Somthing went wrong...')
