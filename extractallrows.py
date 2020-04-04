

from selenium.common.exceptions import NoSuchElementException
from jstorScrap.paid import PAID

class ExtractAllRows:

    all_links = []

    def __init__(self):
        self.scrape_all_links()

    def scrape_all_links(self):
        self.table_rows = self.scrape_table_rows()

        for k, row in enumerate(self.table_rows):
            self.scrape_a_link(row)

    def scrape_table_rows(self):
        return self.driver.find_elements_by_xpath(
            "//li[@class='row result-item']")

    def scrape_a_link(self, row):
        try:
            doc = row.find_element_by_xpath(
                ".//a[@class='pdfLink button']")
        except NoSuchElementException:
            self.all_links.append(Paid(row))
        else:
            self.all_links.append(Free(row))

