from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

captcha = driver.find_element(By.LINK_TEXT, "Try different image")
captcha.click()

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

#driver.close()
driver.quit()