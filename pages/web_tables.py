from pages.base_page import BasePage
from components.components import WebElement

class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.add_button = WebElement(driver, "addNewRecordButton", "id")
        self.dialog = WebElement(driver, "body > div.fade.modal.show > div > div", "css")
        self.submit_button = WebElement(driver, "submit", "id")

        self.first_name = WebElement(driver, "firstName", "id")
        self.last_name = WebElement(driver, "lastName", "id")
        self.email = WebElement(driver, "userEmail", "id")
        self.age = WebElement(driver, "age", "id")
        self.salary = WebElement(driver, "salary", "id")
        self.department = WebElement(driver, "department", "id")

        self.table = WebElement(driver, ".rt-table", "css")
        self.edit_buttons = WebElement(driver, "span[title='Edit']", "css")
        self.delete_buttons = WebElement(driver, "span[title='Delete']", "css")

        self.column_headers = WebElement(driver, ".rt-resizable-header", "css")
        self.header_sort_asc = WebElement(driver, ".rt-resizable-header.sort-asc", "css")
        self.header_sort_desc = WebElement(driver, ".rt-resizable-header.sort-desc", "css")

    def open_add(self):
        self.add_button.click()


    def submit_form(self):
        self.submit_button.click()

    def edit_first_name(self, new_name):
        self.first_name.clear()
        self.first_name.send_keys(new_name)

    def get_last_record_text(self):
        return self.table.get_text()

    def get_records_count(self):
        return len(self.delete_buttons.find_elements())

    def delete_last_record(self):
        delete_buttons = self.delete_buttons.find_elements()
        delete_buttons[-1].click()
