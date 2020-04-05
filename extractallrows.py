
from selenium.common.exceptions import NoSuchElementException
from paid import PAID
from free import FREE


def extractallrows(driver):
    all_docs = []
    scrape_all_links(driver, all_docs)
    return all_docs


def scrape_all_links(driver, all_docs):
    def scrape_a_link(row):
        try:
            row.find_element_by_xpath(
                ".//a[@class='pdfLink button']")
        except NoSuchElementException:
            all_docs.append(PAID(driver, row))
        else:
            all_docs.append(FREE(driver, row))

    def scrape_table_rows():
        return driver.find_elements_by_xpath(
            "//li[@class='row result-item']")

    for k, row in scrape_table_rows():
        scrape_a_link(row)
