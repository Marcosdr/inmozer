# Using html.parser, lxml could be more performant.
#
# See: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
from bs4 import BeautifulSoup


class Parser:

    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_properties(self):
        # TODO: create properties filling all fields
        return [item['data-adid'] for item in self.soup.find_all('article', attrs={'data-adid': True})]

    def get_property_id(self, item):
        return ''
