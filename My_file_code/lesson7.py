from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим картинку с сундуком и получаем значение атрибута valuex
    treasure_img = browser.find_element(By.ID, "treasure")
    x = treasure_img.get_attribute("valuex")
    print(f"Значение x из атрибута: {x}")

    # 2. Вычисляем функцию
    y = calc(x)
    print(f"Ответ: {y}")

    # 3. Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 4. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 5. Выбираем radiobutton "Robots rule!"
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()

    # 6. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # 7. Ждем результат и получаем код из алерта
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Код из алерта: {alert_text}")
    alert.accept()

finally:
    # Закрываем браузер
    time.sleep(2)
    browser.quit()