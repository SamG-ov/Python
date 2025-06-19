from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver as uc
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

# Create Chrome instance using undetected_chromedriver
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=options)

driver.get("http://www.tinder.com")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(4)
google_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[1]/div/div/div/iframe')
google_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(4)
email = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)
sleep(4)
password = driver.find_element(By.XPATH, value='/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)


sleep(80)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

for n in range(100):

    sleep(4)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button")
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)
