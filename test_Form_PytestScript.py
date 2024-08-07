import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Form_Filling.Form_DataDriven import FormDataDriven


@pytest.mark.usefixtures("form_config_setup")
class Test_FormScript:

    @pytest.mark.parametrize("exl_data", FormDataDriven.excel_data1())
    def test_form_submission(self, exl_data):
        self.fill_form(exl_data)
        self.select_gender("Female")
        self.select_student_status()
        self.enter_birthday("22-04-1999")
        self.submit_form()
        self.verify_alert()
        self.driver.refresh()

    def fill_form(self, exl_data):
        self.driver.find_element(By.NAME, "name").send_keys(exl_data["Name"])
        self.driver.find_element(By.NAME, "email").send_keys(exl_data["Email"])
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(exl_data["Phone_No"])

    def select_gender(self, gender):
        self.driver.find_element(By.ID, "exampleFormControlSelect1").click()
        time.sleep(2)
        Option = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        Option.select_by_visible_text(gender)

    def select_student_status(self):
        self.driver.find_element(By.ID, "inlineRadio1").click()

    def enter_birthday(self, date):
        self.driver.find_element(By.NAME, "bday").send_keys(date)
        time.sleep(2)

    def submit_form(self):
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
        time.sleep(2)

    def verify_alert(self):
        self.driver.execute_script("window.scrollTo(0, 0)")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert")))
        alert_element = self.driver.find_element(By.CLASS_NAME, "alert")
        print(alert_element.text)