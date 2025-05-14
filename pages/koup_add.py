from pages.base_page import BasePage
from components.components import WebElement

class KoupAdd(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://the-internet.herokuapp.com/add_remove_elements/')

        self.btn_add = WebElement(driver, 'button[onclick="addElement()"]', 'css')
        self.btns_delete = WebElement(driver, 'button.added-manually', 'css')

    def equal_url(self):
        return self.driver.current_url == self.base_url

