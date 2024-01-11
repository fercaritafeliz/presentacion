from twilio.rest import Client

account_sid="ACb6b5554680b6fc299087c487a3374a28"
auth_token = "b5aab1a22adcc964ac1b705380ab97f8"
client=Client(account_sid,auth_token)
client.messages.create(from_="+18624658749",body="Mensaje de prueba de costo",to="+522213295628")


#este codigo sirve para mandar mensajes pero la neta no me gusta que hay que comprar un número para mandar a numeros no verificados
#sirve como para avisarte cosas por sms
