import ipdb


class Book:

    def __init__(self, title):
        self.title = title

    def turn_page(self):
        print("Turning page ....")

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if (isinstance(value, int)):
            self._page_count = value
        print("Page_count must be an integer")

    page_count = property(get_page_count, set_page_count)


ipdb.set_trace()
