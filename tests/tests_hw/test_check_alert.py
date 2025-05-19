import time
from pages.alerts import Alerts


def test_timer_alert_button(browser):
    page = Alerts(browser)
    page.visit()
    time.sleep(2)

    assert page.timerAlertButton.exist()
    page.timerAlertButton.click()

    time.sleep(6)

    alert = browser.switch_to.alert

    alert.accept()

#для проверки использовал стандартный метод переключения на алерт (еще можно  сделать  получение
# текста алерта,если он имеется в спецификации (и мы его знаем))
#тест провалится с исключением NoAlertPresentException,если не будет активного алерта.

