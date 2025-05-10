from pages.text_box import TextBox
import time


def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    full_name = 'Tony Montana'
    current_address = '3rd Stroiteley Street 25 Apt 12'

    text_box_page.name.send_keys(full_name)
    text_box_page.current_address.send_keys(current_address)

    text_box_page.btn_submit.click()
    time.sleep(2)

    assert text_box_page.name_output.exist()
    assert text_box_page.current_address_output.exist()

    assert full_name in text_box_page.name_output.get_text()
    assert current_address in text_box_page.current_address_output.get_text()