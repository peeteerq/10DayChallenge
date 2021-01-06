# 10 Day Coding Challenge - Day 3
# Title: Mail Sender
"""Description: Program wysyła spersonalizowany mailing do osob z bazy excela.
                W mailu ma byc zalacznik - plik graficzny.
                Program musi byc zabezpieczony przed brakiem excela, brakiem osoby w nim, spamem
                Extra: mail w formie html.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import csv
import ssl
import getpass
import os

port =465

passw = getpass.getpass()
#print(passw)

sender = "sendermail@gmail.com"
receiver = ""

message = MIMEMultipart("alternative")
message["Subject"] = "Attachment"
message["From"] = sender
message["To"] = receiver

def write_text(Imie_i_nazwisko):
    #print(Imie_i_nazwisko)
    global text
    text = """
    Hi """ + Imie_i_nazwisko + """
    How are you?
    Please take a look at attached image.
    BR
    """

# html = """\
# <html>
#   <body>
#     <p>Hi,<br>
#        How are you?<br>
#        <a href="http://www.realpython.com">Real Python</a>
#        has many great tutorials.
#     </p>
#   </body>
# </html>
# """

#part2 = MIMEText(html, "html")
#message.attach(part2)

img_data = open("C:/Users/milek/Pictures/Capture.png", "rb").read()
image = MIMEImage(img_data, name = os.path.basename("C:/Users/milek/Pictures/Capture.png"))
message.attach(image)

context = ssl.create_default_context()

##For localhost server:
# server = SMTP()
# server.connect('localhost', 1025)

with open("C:/Users/milek/Documents/addr.csv") as file:
    reader = csv.reader(file)
    next(reader)    #skip header row
    for Imie_i_nazwisko in reader:
        print("Sending email to " + Imie_i_nazwisko[1])
        write_text(Imie_i_nazwisko[1])
        receiver = Imie_i_nazwisko[0]
        part1 = MIMEText(text, "plain")
        message.attach(part1)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("your_receiver_mail@gmail.com", passw)
            server.sendmail(sender, receiver, message.as_string())
