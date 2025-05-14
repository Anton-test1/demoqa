from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/webtables')


        self.no_data = WebElement(driver, "div.rt-noData", "css")
        self.btn_delete_row = WebElement(driver, "span[title='Delete']", "css")
        self.rows = WebElement(driver, "div.rt-tbody > div[role='row']", "css")


    def delete_rows(self):
        while self.btn_delete_row.exist():
            self.btn_delete_row.click()