import pandas as pd
import smtplib

# v-1

SenderAddress = "russell.cedillo3@gmail.com"
password = "Numz21$hoe"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
print("Done")