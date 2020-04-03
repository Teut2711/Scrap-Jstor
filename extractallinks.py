
class ExtractAllLinks(Jstor):

    all_links = []

    def scrape_all_links(self):
        self.table_rows = self.scrape_table_rows()

        for k, row in enumerate(self.table_rows):
            self.scrape_a_link(row)

        #     except NoSuchElementException:  # exception do nothing
        #         pass
        #     else:
        #         
        #     finally:  # add lnk nd data
        #         

        #     try:
        #         ele = self.driver.find_element_by_xpath(
        #             "//li[@class='pagination-next']/a[@id='next-page']")
        #     except NoSuchElementException:
        #         pass
        #     else:
        #         ele.click()
        #         sleep(3)
        #         self.scrape_all_links()

    def scrape_table_rows(self):
        return self.driver.find_elements_by_xpath(
            "//li[@class='row result-item']")

    def scrape_a_link(self, row):

        try:
            doc = row.find_element_by_xpath(
                    ".//a[@class='pdfLink button']")
        except NoSuchElementException:
            paid.scrap_attribs(row)
        else:
            free.scape_attribs(row)
        finally:
            pass




