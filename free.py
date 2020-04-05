from urllib.parse import urljoin
from templates import GeneralDoc
from utils import helper_try_except


class FREE(GeneralDoc):
    def __init__(self, driver, row):
        super().__init__(row)
        self.PDF = self.makePDF(driver, row)
        self.attributes["PDF"] = self.makePDF(driver, row)

    def makePDF(self, driver, row):
        driver.get(self.scrape_download_link(row))

    @helper_try_except
    def scrape_download_link(self, row):

        doc = row.find_element_by_xpath(
            ".//a[@class='pdfLink button']").get_attribute("href")

        return urljoin(self.driver.parent.current_link, doc)
