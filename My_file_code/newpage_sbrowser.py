from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем страницу
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button =  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Получаем список всех открытых окон
    all_windows = browser.window_handles
    # Переключаемся на новое окно (второе в списке)
    browser.switch_to.window(all_windows[1])

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