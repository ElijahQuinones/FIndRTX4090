import os
from twilio.rest import Client
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


account_sid = 'Your sid goes here'
auth_token = 'your auth token goes here'
client = Client(account_sid, auth_token)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
BB_RTX4090 = "https://www.bestbuy.com/site/searchpage.jsp?st=rtx+4090&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys"
driver.get(BB_RTX4090)
print(driver.title)
ids = driver.find_elements(By.CLASS_NAME, "sku-item")
message = "\n\n"


storeinfo = []
for ii in ids:
    time.sleep(1)
    try:
        title = (ii.find_element(By.CLASS_NAME, 'sku-title').text + "\n\n")
        price=(ii.find_element(By.CLASS_NAME, "price-block").text + "\n\n")
        if "Shop" in price or "Add" in price or "See" in price:
            print(title)
            print(price)
            message = message + title + price + "\n is in stock \n\n"
    except Exception as e:
        print(e)
        print("an error has occured")

driver.quit()

if message == "\n\n":
    message ="nothing is in stock from bestbuy"
message = client.messages.create(
                     body=message,
                     from_='Enter Your Twillo number here',
                     to='Enter your Phone number here'
                 )

print(message.sid)

