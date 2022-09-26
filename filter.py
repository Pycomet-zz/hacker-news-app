from config import *


class Filter:
    def __init__(self, results):
        self.filtered = results.copy()

    def filter_by_type(self, type: str):
        "Filter By News Type - Story, Job or Poll"
        pass

    def filter_by_text(self, text: str):
        "Filter by a text from DB"
        pass
