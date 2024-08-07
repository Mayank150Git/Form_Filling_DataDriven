import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
Service_Obj = Service()
driver = webdriver.Chrome(service= Service_Obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Entering the Filed name:

driver.find_element(By.NAME, "name").send_keys("Mayank") #Data-driven
driver.find_element(By.NAME, "email").send_keys("mayank@yopmail.com") #Data-driven
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123") #Data-driven

#Selecting the Static drop-down:
driver.find_element(By.ID, "exampleFormControlSelect1").click()
time.sleep(2)
Option = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
Option.select_by_visible_text("Female")

# Selecting the radiobuttons:
driver.find_element(By.ID, "inlineRadio1").click()

# Interacting with the calendar element:
driver.find_element(By.NAME, "bday").send_keys("22-04-1999")
time.sleep(2)

# Clicking on the Submit Button:
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
time.sleep(2)

#Capturing the Success alert:

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0)")

# # Maximum number of attempts
# max_attempts = 3
# attempts = 0
#
# while attempts < max_attempts:
#     try:
#         # Wait for the element to be visible
#         wait = WebDriverWait(driver, 10)
#         wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert")))
#
#         # Find and print the element's text
#         alert_element = driver.find_element(By.CLASS_NAME, "alert")
#         print(alert_element.text)
#         break  # Exit the loop if successful
#     except Exception as e:
#         print(f"Attempt {attempts + 1} failed: {e}")
#         attempts += 1
#         time.sleep(2)  # Optional: wait for a short period before retrying
#
# if attempts == max_attempts:
#     print("Failed to find the element after maximum attempts.")


wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert")))
alert_element = driver.find_element(By.CLASS_NAME, "alert")
print(alert_element.text)