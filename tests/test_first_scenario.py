import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

"""
    тест проводится в браузере Chrome
"""


def test_first_scenario():
    browser = webdriver.Chrome()
    browser.get('https://sbis.ru/')

    browser.find_element(By.LINK_TEXT, 'Контакты').click()
    browser.find_element(By.CSS_SELECTOR, "a[href='https://tensor.ru/']").click()
    time.sleep(4)
    browser.switch_to.window(browser.window_handles[1])
    blocks = browser.find_elements(By.CSS_SELECTOR, "p.tensor_ru-Index__card-title.tensor_ru-pb-16")
    time.sleep(10)
    assert any(block.text == "Сила в людях" for block in blocks), "нет"

    try:

        about_link = browser.find_element(By.XPATH,
                                          "//a[@href='/about' and contains(@class, 'tensor_ru-link tensor_ru-Index__link')]")


        browser.execute_script("arguments[0].scrollIntoView(true);", about_link)
        time.sleep(1)
        about_link.click()

    except Exception as e:
        print(f"Exception caught: {e}")

        cookie_button = browser.find_element(By.CSS_SELECTOR, ".tensor_ru-CookieAgreement__button")
        cookie_button.click()

        about_link = browser.find_element(By.XPATH,
                                          "//a[@href='/about' and contains(@class, 'tensor_ru-link tensor_ru-Index__link')]")
        browser.execute_script("arguments[0].scrollIntoView(true);", about_link)
        time.sleep(1)
        about_link.click()

    print(f"Current url: {browser.current_url}")
    time.sleep(5)

    images = browser.find_elements(By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
    first_image_width = images[0].get_attribute('width')
    first_image_height = images[0].get_attribute('height')
    for image in images:
        assert image.get_attribute(
            'width') == first_image_width, f"Картинок {image.get_attribute('src')} разные width"
        assert image.get_attribute(
            'height') == first_image_height, f"Картинок {image.get_attribute('src')} разные height"


