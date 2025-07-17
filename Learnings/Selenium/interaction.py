from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome browser open after program
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

#Find the second anchor tag on another li a
# articles_in_En = driver.find_elements(By.CSS_SELECTOR,'#articlecount ul li a')
# a_list = [item for item in articles_in_En]
# print(f'Articles_count in English: {a_list[1].text}')

# Click the "Content Portal" anchor tag
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the "search" <input> by Name
search = driver.find_element(By.NAME, value="search")
#Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER) #search.send_keys(Keys.ENTER)

#driver.close()
# driver.quit()