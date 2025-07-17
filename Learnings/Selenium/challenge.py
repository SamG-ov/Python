from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
events = {}
upcoming_events_date = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")

upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")

for n in range(len(upcoming_events_date)):

    events[n] = {"time": upcoming_events_date[n].get_attribute("datetime").split("T")[0],"name": upcoming_events_name[n].text}

print(events)

#driver.close()
driver.quit()