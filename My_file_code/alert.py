from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открываем страницу
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку "I want to go on a magical journey!"
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # 2. Принимаем confirm alert
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. Теперь мы на новой странице, где нужно найти x и вычислить ответ
    # Ждем немного для загрузки новой страницы
    time.sleep(1)

    # Находим элемент со значением x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Значение x: {x}")

    # Вычисляем y
    y = calc(x)
    print(f"Ответ: {y}")

    # 4. Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 5. Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 6. Получаем результат из финального алерта
    time.sleep(5)
    alert = browser.switch_to.alert
    print(f"Код из алерта: {alert.text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()