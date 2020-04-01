import _paper_info
import _base64topdf

import re
from selenium.common.exceptions import NoSuchElementException


def scrape(self, k, url):
    self.driver.get(url)
    self.articles[k+1] = {}
    self.articles[k+1]["TITLE"] = _paper_info.title(self)
    self.articles[k+1]["AUTHOR"] = _paper_info.author(self)
    self.articles[k+1]["CITATION"] = _paper_info.citation(self)
    self.articles[k+1]["PUBLISHER"] = _paper_info.publisher(self)
    self.articles[k+1]["JOURNAL"] = _paper_info.journal(self)
    self.articles[k+1]["PAGE COUNT"] = _paper_info.page_count(self)
    self.articles[k+1]["TOPICS"] = _paper_info.topics(self)
    try:
        
        self.driver.find_element_by_xpath(
                """//ul[@class='action-buttons mln']/li/a[contains(text(),
                'Read')][contains(text(), 'Online')]""").click()

    except NoSuchElementException:
        try:
            pdf_url = self.driver.find_element_by_xpath(
                "//a[contains(@class,'pdfLink')]").click()
        except NoSuchElementException:
            print(f"See Page :{self.driver.current_url}")
        else:
            print("Free PDF")
    else:
        self.articles[k+1]["PDF"] = self.scrape_pdf()

""" 
def extract_data(self):

    if pdf_url:
        print("Check url", self.driver.current_url)
        input("Enter to proceed")
        return {}
        # pdf_url = pdf_url[0].get_attribute("href").split(
        # ".pdf?")[0]+".pdf"
        # response = requests.get(urljoin(self.driver.current_url,
        #  pdf_url)).content
        # print("Worked")
        # with open(f"f{self.strange}.pdf", "wb") as f:
        #     f.write(response)
        #     self.strange += 1
    else:
        d = {

        try:


            d.update({"PDF": self.scrape_pdf()})
        except:
            pass
        finally:
            return d """


def scrape_pdf(self):

    images = []
    '''  Add all links '''
    try:
        while True:
            images.append(self.driver.find_element_by_xpath(
                """//img[@id='page-scan-container']
                [contains(@src,'data:image')]""")
            ).get_attribute("src")
            self.driver.find_element_by_xpath(
                "//span[@aria-label='Next Page']").click()
    except:
        title = self.driver.find_element_by_xpath(
            "//h1[@class='medium-heading][@class='item-title']").text
        return _base64topdf.toPDF(title, images)
