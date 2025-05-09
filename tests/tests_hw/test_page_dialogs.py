from pages.modal_dialogs import ModalDialogsPage


def test_modal_elements(browser):
    modal_page = ModalDialogsPage(browser)
    modal_page.visit()
    assert modal_page.btns_submenu.check_count_elements(5)


def test_navigation_modal(browser):
    modal_page = ModalDialogsPage(browser)

    modal_page.visit()

    modal_page.refresh()

    modal_page.icon.click()

    modal_page.back()

    browser.set_window_size(900, 400)

    modal_page.forward()

    assert browser.current_url == 'https://demoqa.com/'

    assert modal_page.get_title() == 'DEMOQA'

    browser.set_window_size(1000, 1000)