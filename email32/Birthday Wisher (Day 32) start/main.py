import smtplib, random
import datetime as dt

with open("quotes.txt", "r") as quote:
    data_into_list = quote.readlines()

today_quote = random.choice(data_into_list)
print(today_quote)

now = dt.datetime.now()
day = now.weekday() + 1
print(day)



my_email = "sparkrayburntesting@gmail.com"
password = "xaeywtratytstvoa"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="abhinavdotkulkarni@gmail.com",
                        msg=f"Subject:Monday Motivation\n\n {today_quote}")
#
#
#
#
