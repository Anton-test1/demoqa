import time
from pages.web_tables import WebTables

def test_column_sort(browser):
    page = WebTables(browser)
    page.visit()
    time.sleep(2)

    headers = page.column_headers.find_elements()

    for header in headers:

        header.click()
        time.sleep(1)
        assert "sort-asc" in header.get_attribute("class")

        header.click()
        time.sleep(1)
        assert "sort-desc" in header.get_attribute("class")


#мы получаем список всех заголовков и перебираем их,кликая,сортируем по возрастанию и убыванию.И
#c помощью get_attribute получаем значения аттрибута (class)
#(Возможна 3 проверка на сброс сортировки по 3 клику,но на нашем сайте сброса нет,а 3 клик просто запускает цикл asc-desc
# заново)