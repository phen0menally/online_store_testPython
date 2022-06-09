import time


def test_is_there_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]'))
    assert button > 0, 'Кнопка "Добавить в корзину" не найдена'
