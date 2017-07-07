from email.mime.text import MIMEText
import smtplib

def send_email(email, height, avg, count):
    from_email = "born2control@gmail.com"
    from_pw = "QWE321qwe321"
    to_email = email

    subject = "Height data that you asked for buddy!"
    message = "Hey there, your height is <strong>%s</strong>. <br> The average height is <strong>%s</strong> out of <strong>%s</strong> entries! <br> Thanks for using <strong>Heightify!</strong>" % (height, avg, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_pw)
    gmail.send_message(msg)
