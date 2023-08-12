from selenium.webdriver.common.by import By


class Test_CredKart_Login_params():

    def test_CredKart_Login_params_003(self, setup, data_for_login):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(data_for_login[0])
        self.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(data_for_login[1])
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            self.driver.save_screenshot(".\\Screenshots\\" + data_for_login[0] + "_" + data_for_login[1] + "_" + "test_CredKart_Login_002_Pass.PNG")
            print('Login TestCase is Passed')
            self.driver.close()
            assert True
        except:
            print('Login TestCase is Failed')
            self.driver.save_screenshot(".\\Screenshots\\" + data_for_login[0] + "_" + data_for_login[1] + "_" + "test_CredKart_Login_002_fail.PNG")
            self.driver.close()
            assert False
