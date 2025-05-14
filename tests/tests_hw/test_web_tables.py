import time
from pages.web_tables import WebTables


def test_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()
    time.sleep(2)

    assert web_tables_page.add_button.visible()
    web_tables_page.add_button.click()
    time.sleep(2)
    assert web_tables_page.dialog.visible()

    web_tables_page.submit_button.click()
    time.sleep(2)
    assert web_tables_page.dialog.visible()

    first_name = 'Tony'
    last_name = 'Montana'
    email = 'ggkach@bk.ru'
    age = '31'
    salary = '1000'
    department = 'IT'
    new_first_name = 'Johny'

    web_tables_page.first_name.send_keys(first_name)
    web_tables_page.last_name.send_keys(last_name)
    web_tables_page.email.send_keys(email)
    web_tables_page.age.send_keys(age)
    web_tables_page.salary.send_keys(salary)
    web_tables_page.department.send_keys(department)
    time.sleep(2)

    web_tables_page.submit_button.click()
    time.sleep(2)

    record_data = web_tables_page.get_last_record_text()
    assert first_name in record_data
    assert last_name in record_data
    assert email in record_data
    assert age in record_data
    assert salary in record_data
    assert department in record_data

    web_tables_page.edit_buttons.find_elements()[-1].click()
    time.sleep(2)
    assert web_tables_page.dialog.visible()

    web_tables_page.edit_first_name(new_first_name)
    time.sleep(2)
    web_tables_page.submit_form()
    time.sleep(2)

    update_text = web_tables_page.get_last_record_text()
    assert new_first_name in update_text
    assert last_name in update_text

    number_of_rows = web_tables_page.get_records_count()
    web_tables_page.delete_buttons.find_elements()[-1].click()
    time.sleep(2)
    assert web_tables_page.get_records_count() == number_of_rows - 1

    #[-1] - последний элемент списка(принимаем,что новые данные выводятся в конец списка,а не сортируются при записи по каким-либо критериям)