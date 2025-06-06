from pages.form_page import FormPage
import time


def test_form_validate(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert form_page.first_name.find_element().get_attribute('placeholder') == 'First Name'
    assert form_page.last_name.find_element().get_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.find_element().get_attribute('placeholder') == 'name@example.com'

    assert form_page.user_email.find_element().get_attribute('pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()
    time.sleep(2)
    assert 'was-validated' in form_page.user_form.get_dom_attribute('class')