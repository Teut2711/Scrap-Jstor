from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin
from .meta import DocsType


class free(DocsType):

    def scrape_download_link(self, row):

        doc = row.find_element_by_xpath(
            ".//a[@class='pdfLink button']").get_attribute("href")

        return urljoin(self.driver.parent.current_link, doc)
