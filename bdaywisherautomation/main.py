import smtplib, random, pandas
import datetime as dt
my_email = "sparkrayburntesting@gmail.com"
password = "xaeywtratytstvoa"




delta = pandas.read_csv("birthdays.csv")
name = delta["name"].to_list()
month = delta["month"].to_list()
day = delta["day"].to_list()
email = delta["email"].to_list()
print(month)

index = 0

now = dt.datetime.now()
thisday = now.day
thismonth = now.month
print(thismonth)
print(thisday)
for m in month:
    if m == thismonth:
        for d in day:
            if d == thisday:
                index = day.index(d)
print(index)

choice = random.randint(1, 3)


with open(f"letter_templates/letter_{choice}.txt") as letter:
    contents = letter.read()
    contents = contents.replace("[NAME]", f"{name[index]}")
    print(contents)







with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email[index], msg=f"Happy_birthdayyyy\n\n{contents}")

























