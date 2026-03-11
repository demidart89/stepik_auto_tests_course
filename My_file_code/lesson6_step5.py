from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим элемент со значением x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print(f"Значение x: {x}")

    # 2. Вычисляем функцию
    y = calc(x)
    print(f"Ответ: {y}")

    # 3. Вводим ответ в текстовое поле (оно вверху, не перекрыто)
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 4. Находим radiobutton "Robots rule!" и прокручиваем до НЕГО
    robots_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)

    # 5. Отмечаем checkbox (он тоже может быть перекрыт)
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 6. Кликаем на radiobutton
    robots_radio.click()

    # 7. Находим кнопку Submit и прокручиваем до неё (если нужно)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # 8. Получаем код из алерта
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Код из алерта: {alert_text}")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()