from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, 'footer span')
    def exist_icon(self):
        return self.icon.exist()

    def click_on_the_btn(self):
        self.btn_elements.click()

    def equal_url(self):
        return self.driver.current_url == self.base_url