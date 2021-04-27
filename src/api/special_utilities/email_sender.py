import sendgrid
from sendgrid.helpers.mail import *

def email_sender (email,password):
    message = Mail(from_email='fpineda1410@gmail.com',
            to_emails=email,
            subject='Recuperación de contraseña Wedding Budgets',
            plain_text_content='and easy todo anywhere',
            html_content='Tu contraseña es la siguiente  '+'<strong>'+password+'</strong>')
  
    sg = sendgrid.SendGridAPIClient(api_key='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')
    response=sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    



    
    