from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert element_page.text_please.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.icon.exist()
    assert element_page.btn_sidebar_first.exist()
    assert element_page.btn_sidebar_first_textbox.exist()