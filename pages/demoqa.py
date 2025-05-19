from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.text_footer = WebElement(driver, '#app > footer > span')
        self.icon = WebElement(driver, '#app > header > a')
        self.h5 = WebElement(driver, 'h5')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

    def exist_icon(self):
        return self.icon.exist()

    def click_on_the_btn(self):
        self.btn_elements.click()

    def equal_url(self):
        return self.driver.current_url == self.base_url


class Radio(BasePage):
    def __init__(self, driver):
        super().__init__(driver, self.base_url)
        self.base_url = 'https://demoqa.com/radio-button'
        self.yes = WebElement(driver, 'label[for="yesRadio"]')
        self.impressive = WebElement(driver, 'label[for="impressiveRadio"]')
        self.no = WebElement(driver, 'label[for="noRadio"]')
        self.text = WebElement(driver, '.text-success')
    def visit(self):
        self.driver.get(self.base_url)

    def click_force(self, element):
        self.driver.execute_script("arguments[0].click();", element)