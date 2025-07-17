import smtplib
import datetime as dt
import random

my_email = "...@gmail.com"
password = "ecfe hwfy bbzc hgvq"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: #If monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="...@mail.ru",
            msg=f"Subject: Monday Motivation\n\n{quote}"
        )
