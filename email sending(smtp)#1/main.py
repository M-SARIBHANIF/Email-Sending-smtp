import smtplib
my_email = "insert email"
password="your email password"
#with smtplib.SMTP("smtp.gmail.com") as connection:
    #connection.starttls()
    #connection.login(user=my_email,password=password)
    #connection.sendmail(from_addr=my_email,to_addrs="enter sender email",msg="Subject:Hello\n\n Body of Email")
    #connection.close()

import datetime
#now = datetime.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#data_of_birt = datetime.datetime(year=1999,month=12,day=14,hour=4)

import random
now = datetime.datetime.now()
weekday = now.weekday()
if weekday ==0:
   with open("quotes.txt") as quote:
       all_quotes = quote.readlines()
       quote = random.choice(all_quotes)
   with smtplib.SMTP("smtp.gmail.com") as connection:
       connection.starttls()
       connection.login(my_email,password)
       connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Monday Motivation\n\n"
                                                                    f"{quote}")
       
