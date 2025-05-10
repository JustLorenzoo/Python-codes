import smtplib
from email.mime.text import MIMEText


sender = 'emailupdates.15@gmail.com'
receiver = 'akungamerenz@gmail.com'
subject = 'Important Update'
body = 'User, Silahkan perbarui informasi akunmu di http://malicious-website.com.'


msg = MIMEText(body)
msg['Subject'] = subject
msg['from'] = sender
msg['To'] = receiver

with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login(sender, 'your_password')
    server.sendmail(sender, receiver, msg.as_string())
    print("Email phising dikirim")