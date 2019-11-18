from craigslist import CraigslistHousing
import search_settings as ss
import os
#from pprint import pprint
import string
import smtplib
from email.message import EmailMessage
#import test_email
import smtplib
import getpass
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def emailFunction(CLList):
    print(CLList)
    print("You have entered function.")

    sender_email = 'mgdevtest@gmail.com'
    receiver_email = 'mgordon25@gmail.com'
    gmail_password = 'fvfu3533'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    print(receiver_email)

    email_text = """\
    From: 
    To: 
    Subject: 


    """ 

    #html = """\

            #<a href="https://sfbay.craigslist.org/pen/apa/d/belmont-unbeatable-value-for-top-floor/7021410954.html">Real Python</a> 

        # """

    email_text2 = str(CLList)
    # -- TODO: Insert text into hyperlink

    # convert to plain/html MIMEText objects
    part1 = MIMEText(email_text, "plain")
    #part2 = MIMEText(html, "html")
    part3 = MIMEText(email_text2, "plain")

    # Add HTML/plain text to MIMEMultipart message
    # the email client will try to render the last part first

    message.attach(part1)
    #message.attach(part2)
    message.attach(part3)



    #try:
    #    gmail_password = input("Password: ")
    
    #except:
    #    print("error")

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, gmail_password)
        server.sendmail(sender_email, receiver_email , message.as_string())
        server.close()
    

        print('Email sent')

    except:
        print('Somthing went wrong...')



    # -- TODO --
#  convert results to list      !!!!!!!!!!!!!!!!!!!!!!!!!done
#  no need for text file        !!!!!!!!!!!!!!!!!!!!!!!!!done
#  make email a function and pass list to it.      !!!!!!done
#  insert list into html and send                  !!!!!!done
#  format links


if os.path.exists('search_results.html'):
    os.remove('search_results.html')
cl = CraigslistHousing(site='sfbay', area=ss.CRAIGSLIST_SUB, category='apa', filters={'max_price': 3000, 'min_price': 2000})

results = []
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)



print(type(results))
lineList = list()
    
for result in results:
    search_results = open('search_results.html', 'a+')
    search_results.write(result["url"] + "\n")

print(str(search_results)   )



    
lineList = [line.rstrip('\n') for line in open('search_results.html')]



for result in results:
    lineList.append(result["url"])
    
#print(type(lineList))

#for line in lineList:
    
#    print(line)


emailFunction('\r\n'.join(lineList))
