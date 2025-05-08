from pages.demoqa import DemoQa
from components.components import WebElement


def test_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    footer = WebElement(browser, 'footer span')
    assert footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_center_text_on_elements_page(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_btn()
    center_text = WebElement(browser, '#app > div > div > div > div.col-12.mt-4.col-md-6')#локатор определил через dev tools
    assert center_text.get_text() == 'Please select an item from left to start practice.'