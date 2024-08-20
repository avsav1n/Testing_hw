import os
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def test_auth_yaid():
    '''Тест проверки авторизации на сайте https://passport.yandex.ru/auth/
    '''
    path = ChromeDriverManager().install()
    options = Options()
    options.add_experimental_option('detach', True)
    browser_service = Service(executable_path=path)
    driver = Chrome(service=browser_service, options=options)
    
    driver.get('https://passport.yandex.ru/auth/')

    # Ввод логина
    login_field = driver.find_element(
        By.CLASS_NAME, 'Textinput-Control')
    login_field.send_keys(f'{os.getenv('YALOGIN')}@yandex.ru')
    driver.find_element(By.ID, 'passp:sign-in').click()
    sleep(2)

    # Ввод пароля
    password_field = driver.find_element(
        By.ID, 'passp-field-passwd')
    password_field.send_keys(os.getenv('YAPASS'))
    driver.find_element(By.ID, 'passp:sign-in').click()
    sleep(40)
    # В связи с необходимостью подтверждения через код из смс (или пуш-уведомления)
    # данный этап выполняется вручную

    # Проверка входа
    # Осуществляется сверка логина, отображаемого на главной странице профиля
    field_for_checking = driver.find_elements(
        By.CLASS_NAME, 'Text_root__J8eOj.bulleted-list-item_root__1Y90C')[-1].text
    assert field_for_checking == os.getenv('YALOGIN')
