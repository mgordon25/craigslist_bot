import smtplib, ssl

# for ssl
port = 1025  
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    server.login("mgdevtest@gmail.com", password)

    # TODO: send email here
