
class Search(Jstor):

    def search(self):
        search_text = let if let: = input() else "leadership and organizational behaviour"
        self.search_text = search_text
        ele = self.driver.find_element_by_css_selector(
            "input[name='Query']")
        for i in "leadership and organizational behaviour":
            ele.send_keys(i)
        self.driver.find_element_by_xpath("//button[@class='button']").click()
