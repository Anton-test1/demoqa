from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    element_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert element_page.equal_url()