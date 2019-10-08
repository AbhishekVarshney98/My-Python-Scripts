import pandas as pd

file=pd.read_excel("ContactNo.xlsx")

ext=file.iloc[:,1:]
arrTolist=ext.values.tolist()

listTostr=str(arrTolist)[1:-1]

strContact=listTostr.replace('], [',',').replace('[','').replace(']','')

finalContactList = strContact.split(",")
#print(finalContactList)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import autoit
except:
    pass
import time
import datetime
import os

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None

doc_filename = None
unsaved_Contacts = None

def input_contacts():
    global unsaved_Contacts
    # List of Contacts
    unsaved_Contacts = finalContactList
    print("Taking the contact list")
    print(unsaved_Contacts)
    

def input_message():
    global message
    # Enter your message
    print()
##    message = input("Enter your message: \n")
    message= 'bot message...no need to reply'
##    print("You entered --- " + message)

def whatsapp_login():
    global wait,browser,Link
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    browser.maximize_window()
    print("QR scanned")


def send_unsaved_contact_message():
    global message
    try:
        time.sleep(10)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")

    except NoSuchElementException:
         print("Failed to send message")
    return

def sender():
    global Contact, unsaved_Contacts
    if len(unsaved_Contacts)>0:
        for i in unsaved_Contacts:
            link = "https://wa.me/"+i
            browser.get(link)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="action-button"]').click()
            time.sleep(2)
            print("Sending message to", i)
            send_unsaved_contact_message()
            time.sleep(3)

if __name__ == "__main__":

    print("Start")

    # Taking contact list as input to send messages
    input_contacts()
    # Enter the message you want to send
    input_message()

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()

    # Send message to all Contact List
    sender()

    # message sending Task Complete
    print("Task Completed")
