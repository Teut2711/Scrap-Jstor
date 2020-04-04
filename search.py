
class Search:
    def __init__(self):
        self.search()

    def search(self):
        ele = self.driver.find_element_by_css_selector(
            "input[name='Query']")
        for i in self.search_text:
            ele.send_keys(i)
        self.driver.find_element_by_xpath("//button[@class='button']").click()
