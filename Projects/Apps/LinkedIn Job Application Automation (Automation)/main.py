from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]

def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-button--secondary")[1]
    discard_button.click()

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # optional
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4238548819&f_AL=true&f_WT=2&geoId=92000000&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# # Click Sign in Button
time.sleep(10)
x_button = driver.find_element(By.CLASS_NAME, value="artdeco-icon")
x_button.click()

sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()
            second_button = driver.find_element(by=By.LINK_TEXT, value="Next")
            second_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()