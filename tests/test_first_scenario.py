from selenium import webdriver
from selenium.webdriver.common.by import By

"""
    тест проводится в браузере Chrome
"""


def test_first_scenario():
    browser = webdriver.Chrome()
    browser.get('https://sbis.ru/')

    browser.find_element(By.LINK_TEXT, 'Контакты').click()
    browser.find_element(By.CSS_SELECTOR, "a[href='https://tensor.ru/']").click()
