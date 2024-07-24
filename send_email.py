import smtplib

sender_email="kuntaljii71@gmail.com"
receiver_email="ranjit.upflairs@gmail.com"

subject="E-MAIL BY PYTHON"
message="""Good Evening Sir!

   
Name : PREETI KUNTAL
Branch : AI & DS
College : Arya College of Engineering
College city : RIICO Industrial Area,  Kukas, Jaipur


"""

text=f"Subject: {subject}\n\n{message}"

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender_email,"xltiyzmzdsydexha")
server.sendmail(sender_email,receiver_email,text)

print("Email has sent successfully")
