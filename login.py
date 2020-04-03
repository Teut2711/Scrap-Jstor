class Login(Jstor):

    def log_me_in(self):
        ele = self.driver.find_element_by_xpath("//input[@name='login']")
        ele.click()
        for i in "apple2711":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath("//input[@name='password']")
        ele.click()
        for i in "abcdefg0":
            ele.send_keys(i)
        ele = self.driver.find_element_by_xpath(
            "//input[@name='submit']").click()



