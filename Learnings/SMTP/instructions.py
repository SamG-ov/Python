import smtplib

my_email = "...@gmail.com"
password = "ecfe hwfy bbzc hgvq"
# got the password by going into the gmail settings -> Security -> App passwords -> and then create a name -> grab the password

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #makes the message encrypted
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="...@mail.ru", msg="Subject:Just saying Hello\n\nHello Bro, this is the body")
connection.close()

#Another way - without having to close the connection
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls() #makes the message encrypted
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email, to_addrs="...@mail.ru", msg="Subject:Just saying Hello\n\nHello Bro, this is the body")


import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday() #0=Monday, 1=Tuesday ...
