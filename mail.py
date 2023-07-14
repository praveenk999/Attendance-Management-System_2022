# import csv

# with open("Attendance.csv") as file:
#     reader = csv.reader(file)
#     next(reader)  # Skip header row
#     for name, email, grade in reader:
#         print(f"Sending email to {name}")
#         # Send email here
        
import csv, smtplib, ssl

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "xxxxx"
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("mv21ecb0b33@student.nitw.ac.in", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )        