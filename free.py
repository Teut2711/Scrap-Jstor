from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin


class free(Jstor, ExtractAllLinks):

    @staticmethod
    def helper_try_except(fun):
        def inner_func(*args):
            try:
                return fun(*args)

            except NoSuchElementException:
                return None
        return inner_func

    @property
    def title(self):
        return self.title

    @property
    def authors(self):
        return self.authors

    @property
    def citation(self):
        return self.citation

    @property
    def topics(self):
        return self.topics

    @property
    def download_link(self):
        return self.download_link

    @property
    def page_link(self):
        return self.pagelink

    @title.setter
    def title(self, row):
        return self.scrape_title(row)

    @authors.setter
    def authors(self, row):
        return self.scrape_authors(row)

    @citation.setter
    def citation(self, row):
        return self.scrape_citation(row)

    @topics.setter
    def topics(self, row):
        return self.scrape_topics(row)

    @download_link.setter
    def download_link(self, row):
        return self.scrape_download_link(row)

    @page_link.setter
    def page_link(self, row):
        return self.scrape_pagelink(row)

    @property
    def attributes(self):
        return dict(
            TITLE=self.title,
            AUTHORS=self.authors,
            CITATION=self.citation,
            TOPICS=self.topics,
            DOWNLOAD_LINK=self.download_link,
            PAGE_LINK=self.pagelink
        )

    @helper_try_except
    def scrape_title(self, ele):

        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        name = current_tag.text
        return name

    @helper_try_except
    def scrape_authors(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='contrib']//descendant::a")
        authors = [j.text for j in current_tag]
        return authors

    @helper_try_except
    def scrape_citation(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='src break-word']")
        citation = current_tag.text
        return citation

    @helper_try_except
    def scrape_topics(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='topic-evaluation-pane mtm']//descendant::a")
        tags = [j.text for j in current_tag]
        return tags

    @helper_try_except
    def scrape_pagelink(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url

    @helper_try_except
    def scrape_download_link(self, row):

        doc = row.find_element_by_xpath(
            ".//a[@class='pdfLink button']").get_attribute("href")

        return urljoin(self.driver.parent.current_link, doc)
