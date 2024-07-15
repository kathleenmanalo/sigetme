from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure
account_sid = 'AC29abd31ed1001853f2992693605d2aac'
auth_token = '02f95b3f405200cd74eb6a22bcf1db4b'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="MENSAJE DE PRUEBA",
                     from_='+19166654785',
                     to='+573108747724'
                 )

print(message.sid)


# import os, math
#
# capital_depositado = 500*3800
# tasa_de_interes = 1
# tiempo = 1
# monto=math.pow(1.0+tasa_de_interes/100,tiempo)*capital_depositado
# interes_compuesto=monto-capital_depositado
# print ('Valor de Monto depositado: ' + repr (capital_depositado))
# print ('Valor de interes compuesto: ' + repr (interes_compuesto))
# print ('Valor de monto final: ' + repr (monto))