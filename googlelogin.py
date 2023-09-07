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
driver.get('https://google.com/')
driver.maximize_window()
sign_in_link = driver.find_elements('xpath',"//a[@href]")
for link in sign_in_link:
    if "Sign in" in link.get_attribute("innerHTML"):
        link.click()
        break
    
email = driver.find_element('xpath', '//*[@id="identifierId"]')
email.send_keys("nandhini.ec21@bitsathy.ac.in")
email_submit = driver.find_element('xpath','//*[@id="identifierNext"]/div/button/span')
email_submit.click()

wait = WebDriverWait(driver,10)
psword = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
psword.send_keys("@nandyN2412")
psword_submit = driver.find_element('xpath', '//*[@id="passwordNext"]/div/button/span')
psword_submit.click()


wait = WebDriverWait(driver, 3)
input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
input.send_keys("Jaiprasad")
input.submit()

