import requests
from bs4 import BeautifulSoup
import re

CLEANR = re.compile('<.*?>')


class Codes:
    """
    Represents a list of codes taken from the initialized URL
    """
    def __init__(self):
        self._codes_list = []
        self._url = ""
        self._page = requests.get(self._url)
        self._data = BeautifulSoup(self._page.content, "html.parser")
        # Upon initialization, add codes to self._codes_list
        entry_elements = self._data.find("div", class_="entry-content")
        ultags = entry_elements.find_all("ul")
        for litag in ultags[1].find_all("li"):
            code_string = str(litag)
            rewards = code_string.split()[1]
            code = code_string.split()[0]
            # Remove HTML tags from the codes
            cleantext = re.sub(CLEANR, '', code)
            self._codes_list.append(cleantext)


    def check_status(self):
        """Function returns True if the website has updated since last check, otherwise False"""
        new_codes_list = []
        new_entry_elements = self._data.find("div", class_="entry-content")
        new_ultags = new_entry_elements.find_all("ul")
        for new_litag in new_ultags[1].find_all("li"):
            code_string = str(new_litag)
            rewards = code_string.split()[1]
            code = code_string.split()[0]
            cleantext = re.sub(CLEANR, '', code)
            new_codes_list.append(cleantext)
        # Compare new_codes_list with self._codes_list to see if site has new codes
        for code in new_codes_list:
            if code not in self._codes_list:
                self._codes_list = new_codes_list
                return True
        return False

    def print_codes(self):
        """Stores the codes in a text file"""
        if self.check_status() is True:
            with open('codes.txt', 'w') as codes:
                for code in self._codes_list:
                    codes.write(code)

    def return_codes(self):
        """Returns list of current codes"""
        return self._codes_list
