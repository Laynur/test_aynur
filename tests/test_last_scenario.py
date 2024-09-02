import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

"""
    3. Сценарий.
    Тест проводится в браузере Chrome
    Проверка загрузки плагина
"""


def test_last_scenario():
    folder_test_project = "C:/tensor_test_aynur"
    option_browser = Options()
    option_browser.add_experimental_option("prefs", {
        "download.default_directory": folder_test_project,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    browser = webdriver.Chrome(options=option_browser)
    browser.get('https://sbis.ru/')
    time.sleep(10)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    cookie_button = browser.find_element(By.CSS_SELECTOR, ".sbis_ru-CookieAgreement__close")
    cookie_button.click()
    browser.find_element(By.LINK_TEXT, "Скачать локальные версии").click()

    browser.find_element(By.CSS_SELECTOR, 'a[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"').click()

    time.sleep(20)