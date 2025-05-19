from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_submenu = WebElement(driver, 'div.element-list.collapse.show > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.small_modal_close = WebElement(driver, '#closeSmallModal')
        self.large_modal_close = WebElement(driver, '#closeLargeModal')
        self.modal_content = WebElement(driver, '.modal-content')