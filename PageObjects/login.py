from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@aria-label='Username']")
    signin = (By.XPATH, "//span[text()='Sign in']")
    password = (By.XPATH, "//input[@aria-label='Password']")
    RegisterSecuritizer = (By.XPATH, "//div[text()='Register Securitizer']")
    Name = (By.XPATH, "//input[@aria-label='Name'][1]")
    Address = (By.XPATH, "//input[@aria-label='Address'][1]")
    PhoneNumber = (By.XPATH, '//input[@aria-label="Phone Number"][1]')
    ZipCode = (By.XPATH, '//input[@aria-label="Zip Code"]')
    Fname = (By.XPATH, '//input[@aria-label="First Name"]')
    Lname = (By.XPATH, '//input[@aria-label="Last Name"]')
    Email = (By.XPATH, '//input[@aria-label="Email Address"]')
    MobileNumber = (By.XPATH, '//input[@aria-label="Mobile Phone"]')
    password1 = (By.XPATH, '(//input[@type="password"])[1]')
    confirmPass = (By.XPATH, '(//input[@type="password"])[2]')
    submit = (By.XPATH, '//button[@type="submit"]')

    def Login_username(self):
        return self.driver.find_element(*Login.username)

    def Login_SignIn(self):
        return self.driver.find_element(*Login.signin)

    def Login_password(self):
        return self.driver.find_element(*Login.password)

    def Login_RegisterSecuritizer(self):
        return self.driver.find_element(*Login.RegisterSecuritizer)

    def Login_Name(self):
        return self.driver.find_element(*Login.Name)

    def Login_Address(self):
        return self.driver.find_element(*Login.Address)

    def Login_PhoneNumber(self):
        return self.driver.find_element(*Login.PhoneNumber)

    def Login_ZipCode(self):
        return self.driver.find_element(*Login.ZipCode)

    def Login_Fname(self):
        return self.driver.find_element(*Login.Fname)

    def Login_Lname(self):
        return self.driver.find_element(*Login.Lname)

    def Login_Email(self):
        return self.driver.find_element(*Login.Email)

    def Login_MobileNumber(self):
        return self.driver.find_element(*Login.MobileNumber)

    def Login_password1(self):
        return self.driver.find_element(*Login.password1)

    def Login_ConfirmPass(self):
        return self.driver.find_element(*Login.confirmPass)

    def Login_Submit(self):
        return self.driver.find_element(*Login.submit)


