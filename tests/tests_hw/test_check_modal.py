import time
from pages.modal_dialogs import ModalDialogsPage


def test_modal_buttons_existence(browser):
    page = ModalDialogsPage(browser)
    page.visit()
    time.sleep(2)

    assert page.small_modal_btn.exist()
    assert page.large_modal_btn.exist()

def test_small_btn(browser):
    page = ModalDialogsPage(browser)
    page.visit()
    time.sleep(1)

    page.small_modal_btn.click()
    time.sleep(2)

    assert page.small_modal_content.visible()
    page.small_modal_close.click()
    time.sleep(1)
    assert page.small_modal_content.hide()

def test_large_btn(browser):
    page = ModalDialogsPage(browser)
    page.visit()
    time.sleep(1)

    page.large_modal_btn.click()
    time.sleep(2)

    assert page.large_modal_content.visible()
    page.large_modal_close.click()
    time.sleep(2)
    assert page.large_modal_content.hide()
