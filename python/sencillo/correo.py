import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http.client import HTTPConnection

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
        # with open('correo.html','wb') as f:
        #     mail_content=f.read()
        #     print('-'*25)
        #     print(mail_content)
        #     print('-'*25)
conec=HTTPConnection( "127.0.0.1:5000/correo")
conec.request('GET','/')
resultado=conec.getresponse()
mail_content=resultado.read()
print('-'*25)
print(mail_content)
print('-'*25)
mail_content=str(mail_content)
sender_address = ''
sender_pass = ''
server.login(sender_address,sender_pass)
receiver_address = ''
print('Aquí se esta enviando un correo')
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'aca el html'   
message.attach(MIMEText(mail_content, 'html'))
text = message.as_string()
server.sendmail(sender_address,receiver_address,text)
server.quit()

#Esto sirve en el flask pero debe existir la pagina de donde se toma el html