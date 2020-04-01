
import re


def title(self):
    try:
        return self.driver.find_element_by_xpath(
            """//h1[contains(@class, 'title')]
            [contains(@class, 'medium-heading')]""").text
    except:
        return None


def author(self):
    try:
        authors = self.driver.find_element_by_xpath(
            "//div[contains(@class,'contrib')]").text
        return [i for i in map(lambda x: x.strip(), authors.replace(
            " and ", " ").split()) if i is not None]
    except:
        return None


def citation(self):
    try:
        return self.driver.find_element_by_xpath(
            "//div[@class='src break-word mbl']").text
    except:
        return None


def publisher(self):
    try:
        return self.driver.find_element_by_xpath(
            "//div[@class='publisher']/a").text.replace(
                "Published", "").replace("by:", "").strip()
    except:
        return None


def journal(self):
    try:
        return self.driver.find_element_by_xpath(
            "//div[@class='journal']").text
    except:
        return None


def page_count(self):
    try:
        return int(re.findall(r"\d+",
                              self.driver.find_element_by_xpath(
                                  "//div[@class='count']").text)[0])
    except:
        return None


def topics(self):
    try:
        return [i.text for i in self.driver.find_elements_by_xpath(
            "//div[contains(@class,'topics')]/a")]
    except:
        return None
