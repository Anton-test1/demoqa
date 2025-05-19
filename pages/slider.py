from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.keys import Keys

class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.slider = WebElement(driver, '.range-slider')
        self.inp = WebElement(driver, '#sliderValue')

    def set_slider_value(self, target_value):
        while int(self.inp.get_dom_attribute('value')) != target_value:
            key = Keys.ARROW_RIGHT if int(self.inp.get_dom_attribute('value')) < target_value else Keys.ARROW_LEFT
            self.slider.send_keys(key)
        return True