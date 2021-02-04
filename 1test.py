import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging

path = os.path.dirname(os.path.realpath(__file__))
driver_path = f'{path}/Modules/chromedriver_win32/chromedriver.exe'     # Путь до драйвера

# Настройка логов
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    datefmt='%m-%d %H:%M:%S',
                    filename='1test.log',
                    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Настройки драйвера
options = Options()
# options.headless = True    # Опция для отключения отображения окна браузера

# Дополнительно
t = 5   # Время для ручной отладки

while True:
    browser = webdriver.Chrome(
        executable_path=driver_path, options=options)
    try:
        logging.info("#####Начало#####")
        url = r'https://www.google.ru/'
        browser.maximize_window()
        browser.get(url)
        time.sleep(t)   # Таймер для ручной отладки
        window_before = browser.window_handles[0]
        browser.switch_to.window(window_before)

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="searchform"]')))
        raise Exception()
        logging.info("Форма поиска отображается")
        time.sleep(t)   # Таймер для ручной отладки

        browser.find_element_by_xpath('//input[@class="gLFyf gsfi"]').send_keys("Тест")
        logging.info('Форма ввода заполняется')

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@class="gNO89b"]'))).click()
        logging.info('Кнопка поиска работает')

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '// div[@id = "rso"]')))
        logging.info('Результаты поиска отображаются')

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="yuRUbf"]'))).click()
        logging.info('Переход по первой ссылке')

        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        time.sleep(t)   # Таймер для ручной отладки
        browser.close()
        time.sleep(t)   # Таймер для ручной отладки
        browser.switch_to.window(window_before)

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="logo"]'))).click()
        logging.info('Переход к основной странице по кнопке "Google"')
        time.sleep(t)   # Таймер для ручной отладки

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="fsl"]/a[1]'))).click()
        logging.info('Переход по ссылке "Реклама"')
        window_before = browser.window_handles[0]

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@class="inner-wrapper"]')))
        logging.info('Информация по рекламе отображается')
        time.sleep(t)   # Таймер для ручной отладки

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="h-c-footer__logo-img"]'))).click()
        logging.info('Возвращение на главную страницу')
        time.sleep(t)   # Таймер для ручной отладки

        window_after = browser.window_handles[1]
        browser.close()
        browser.switch_to.window(window_after)

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="fsl"]/a[2]'))).click()
        logging.info('Переход по ссылке "Для бизнеса"')

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="section-hero-copy col-6"]')))
        logging.info('Информация для бизнеса отображается')
        time.sleep(t)   # Таймер для ручной отладки

        browser.get(url)
        logging.info('Возвращение на главную страницу')
        time.sleep(t)   # Таймер для ручной отладки

    except Exception as e:
        time.sleep(t)
        browser.save_screenshot("err.png")
        logging.error("Ошибка!", exc_info=e)
        browser.quit()

    finally:
        logging.info("#####Конец#####")
        browser.quit()
