
class free(Jstor, ExtractAllLinks):

    def helper_try_except(fun):
        def inner_func():
            try:
                return fun()
            except:
                return None
        inner_func()        

    def scrape_attribs(self, row):

        self.title = self.scrape_title
        self.authors = self.scrape_authors
        self.citation = self.scrape_citation
        self.topics = self.scrape_topics

        for (key, value) in d.items():
            try:
                d[key] = value(ele)
            except NoSuchElementException:
                d[key] = None
        return d

    def scrape_title(self, ele):

        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        name = current_tag.text
        return name

    def scrape_authors(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='contrib']//descendant::a")
        authors = [j.text for j in current_tag]
        return authors

    def scrape_citation(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='src break-word']")
        citation = current_tag.text
        return citation

    def scrape_topics(self, ele):
        current_tag = ele.find_elements_by_xpath(
            ".//div[@class='topic-evaluation-pane mtm']//descendant::a")
        tags = [j.text for j in current_tag]
        return tags

    def scrape_pagelink(self, ele):
        current_tag = ele.find_element_by_xpath(
            ".//div[@class='title']//descendant::a")
        href = current_tag.get_attribute("href")
        url = urljoin(ele.parent.current_url, href)
        return url

    def download_pdf(self):
        pass self.articles[k+1] = {"site_link": self.page_link(row)}
        self.articles[k+1].update(self.scrap_info(row))
        self.total_articles_scraped += 1
        if self.total_articles_scraped ==\
                self.total_articles_to_scrape:
            return None
