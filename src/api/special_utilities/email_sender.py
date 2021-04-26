from sendgrid.helpers.mail import *

def email_sender (email,password):
    sg = sendgrid.SendGridAPIClient("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")
    from_email = Email("fpineda1410@gmail.com")
    to_email = To("fpineda1410@gmail.com")
    subject = ""
    content = Content("text/plain", "Su contraseña es {}".format(password))
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)