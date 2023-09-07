import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://tmp.smounesh.in/list')
driver.maximize_window()

count = 1
driver.implicitly_wait(3)
links = driver.find_element("xpath",'//*[@id="nav"]/a[1]')
links.click()

for i in range(10):
    time.sleep(1)
    dropdownbox = driver.find_elements(by = By.TAG_NAME, value = "option")
    for i in range(len(dropdownbox)):
        if(dropdownbox[i].text == "1 minute"):
            dropdownbox[i].click()
            break
    time.sleep(1.5)
    text = driver.find_element('xpath','//*[@id="content-input"]')
    text.send_keys(f"Hi Hello {count}")
    count = count + 1
    submit = driver.find_element('xpath','//*[@id="submit-button"]')
    submit.click()
    time.sleep(1.5)
    links = driver.find_element("xpath",'//*[@id="nav"]/a[1]')
    links.click()
    time.sleep(1.5)

links = driver.find_element("xpath",'//*[@id="nav"]/a[2]')
links.click()
time.sleep(1)
