import smtplib

myEmail = "javapy4@gmail.com"
passwords = "uecxqihxukjmwslm"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myEmail,password=passwords)
    connection.sendmail(from_addr=myEmail,
                        to_addrs="damlevan409nd@gmail.com",
                        msg="Subject:Phuong\ntest"
                        )
    connection.close()