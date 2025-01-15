# Enviar Email con Tkinter

import smtplib

sender = 'sender@example.com'
receiver = "receiver@example.com"
password = 'password'

subject = 'prueba de correo electronico en python'
body = 'Hola, este es un mensaje de prueba'

message = f"""
    From: Aprende a programar{sender}
    to: emA{receiver}
    Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logeando...")
    server.sendmail(sender, receiver, message)
    print("El correo electronico ha sido enviado...")
except smtplib.SMTPAuthenticationError:
    print("No se pudo iniciar sesion")