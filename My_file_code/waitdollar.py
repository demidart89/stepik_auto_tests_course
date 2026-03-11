from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Используем ссылку из условия (если она верна)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ожидаем появления цены $100 (ждать минимум 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    print("Цена достигла $100! Бронируем...")

    # 2. Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # 3. Решаем математическую задачу на новой странице
    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем ответ
    y = calc(x)
    print(f"x = {x}, ответ = {y}")

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отправляем форму
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    # 4. Получаем результат из алерта
    time.sleep(2)
    alert = browser.switch_to.alert
    print(f"Код из алерта: {alert.text}")
    alert.accept()

finally:
    time.sleep(2)
    browser.quit()