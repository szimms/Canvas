#!/usr/bin/env python
from selenium import webdriver
import time
import datetime
import smtplib
from email.message import EmailMessage
import os


# Finding the day of the week
dayOfWeek = datetime.datetime.today().weekday()

x = datetime.datetime.now()
currentDay = x.strftime("%A")
month = x.strftime("%B")
dateNum = x.strftime("%d")

# Loging into my grades
def school():

    # Logins for school
    username = "******"
    password = "****"

    # Find Infinite Campus(my online power school)
    driver.get("****")

    # Find Username box and Password Box
    username_textbox = driver.find_element_by_id("username")
    password_textbox = driver.find_element_by_id("password")

    # Enter My username and password
    username_textbox.send_keys(username)
    password_textbox.send_keys(password)

    # Hit the login button
    login_button = driver.find_element_by_tag_name("input")
    login_button.submit()

    time.sleep(10)

    # take a ss of classes
    picture = driver.save_screenshot("ClassesForToday.png")



# Function for sending email

def sendMail():
    # Sending Email Info
    EMAIL_ADDRESS = "****@gmail.com"
    EMAIL_PASS = "****"

    #Recieving Email
    SCHOOL_EMAIL = '***'

    msg = EmailMessage()
    msg['Subject'] = 'Classes for %s, %s %s' % (currentDay, month, dateNum)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = SCHOOL_EMAIL
    msg.set_content("Solomon's classes for today!")

    with open('ClassesForToday.png', 'rb') as content_file:
        content = content_file.read()

    msg.add_attachment(content, maintype='image', subtype='png', filename='ClassesForToday')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
        smtp.send_message(msg)


# If the time is correct log into my grades. Take the picture. Compile it into an email and then send the email
if datetime.datetime.now().hour <9:
    # declaring where webdriver is located on my computer
    PATH = "/Users/solomonzimm/Desktop/Programming/pprojects/chromedriver"
    driver = webdriver.Chrome(PATH)
    school()
    time.sleep(3)
    driver.close()
    sendMail()
    time.sleep(5)
    #Remove file from my computer
    if os.path.exists("ClassesForToday.png"):
        try:
            os.remove("ClassesForToday.png")
        except:
            print("no file found")
else:
    print("Invalid Time")
