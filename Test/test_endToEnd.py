import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.login import Login
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self, setup):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//input[starts-with(@aria-label,"Username")]'))
        )

        login = Login(self.driver)
        login.Login_username().send_keys("admin@email.com")
        login.Login_SignIn().click()
        time.sleep(2)
        login.Login_password().send_keys("pinglend")
        login.Login_SignIn().click()
        time.sleep(5)
        login.Login_RegisterSecuritizer().click()
        time.sleep(5)
        login.Login_Name().send_keys("Hello")
        login.Login_Address().send_keys("address")
        login.Login_PhoneNumber().send_keys("29379748743")
        login.Login_ZipCode().send_keys("784748")
        fname = login.Login_Fname()
        self.driver.execute_script("arguments[0].scrollIntoView();", fname)
        time.sleep(2)
        login.Login_Fname().send_keys("firstName")
        login.Login_Lname().send_keys("lastName")
        login.Login_Email().send_keys("email@email.com")
        login.Login_MobileNumber().send_keys("8976856473")
        login.Login_password1().send_keys("Hello@1234")
        login.Login_ConfirmPass().send_keys("Hello@1234")
        login.Login_Submit().click()
        time.sleep(5)
