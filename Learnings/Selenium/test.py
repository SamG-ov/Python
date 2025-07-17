from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome browser open after program
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

#Find the "search" <input> by Name
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CLASS_NAME, value="btn")
#submit = driver.find_element(By.CSS_SELECTOR, value="form button")


#Sending keyboard input to Selenium
fname.send_keys("Python", Keys.TAB)
print("Name Success")
lname.send_keys("Is the best", Keys.TAB)
print("Last name Success")
email.send_keys("pythonmail@gmail.com", Keys.TAB)
print("Email Success")
submit.send_keys(Keys.ENTER)
print("Success")




#driver.close()
# driver.quit()