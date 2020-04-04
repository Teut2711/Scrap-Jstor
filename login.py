
class Login:

    def __init__(self):

        self.feed_id()
        self.feed_password()
        self.submit()

    def feed_id(self):
        ele = self.driver.find_element_by_xpath("//input[@name='login']")
        ele.click()
        for i in self.username:
            ele.send_keys(i)

    def feed_password(self):
        ele = self.driver.find_element_by_xpath("//input[@name='password']")
        ele.click()
        for i in self.password:
            ele.send_keys(i)

    def submit(self):
        self.driver.find_element_by_xpath(
            "//input[@name='submit']").click()
