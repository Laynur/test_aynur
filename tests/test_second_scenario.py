import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
    тест проводится в браузере Chrome
    По умолчанию г. Москва
"""


def test_second_scenario():
    browser = webdriver.Chrome()
    browser.get('https://sbis.ru/')

    browser.find_element(By.LINK_TEXT, 'Контакты').click()
    time.sleep(5)

    my_region_element = browser.find_elements(By.XPATH,
                                             "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
    print(my_region_element[0].text)
    assert my_region_element[0].text == "г. Москва"
    list_partner = browser.find_element(By.CSS_SELECTOR, 'div[data-qa="items-container"]')
    partners = list_partner.find_elements(By.CSS_SELECTOR, ".controls-ListView__itemV-relative.controls-ListView__itemV.controls-ListView__item_default.controls-ListView__item_contentWrapper.js-controls-ListView__editingTarget.controls-ListView__itemV_cursor-pointer.controls-ListView__item_showActions.js-controls-ListView__measurableContainer.controls-ListView__item__unmarked_default.controls-ListView__item_highlightOnHover.controls-hover-background-default.controls-Tree__item")
    assert len(partners) > 0

