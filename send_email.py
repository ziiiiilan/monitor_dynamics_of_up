import smtplib
import ssl
from email.message import EmailMessage
email_address="your_email"
email_password="your_password"
receiver_address="your_email"

context=ssl.create_default_context()
smtp=smtplib.SMTP_SSL("smtp.163.com",465,context=context)
smtp.login(user=email_address,password=email_password)

subject="Python email subject"
body="今日up主动态更新情况"
msg=EmailMessage()
msg["subject"]=subject
msg["From"]=email_address
msg["To"]=receiver_address
msg.set_content(body)
filename=r"D:\develop\code\check_results.txt"
with open(filename,"r",encoding="UTF-8") as f:
    filedata=f.read()

msg.add_attachment(filedata,filename=filename)

smtp.send_message(msg=msg)
smtp.quit()