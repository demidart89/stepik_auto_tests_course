from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    # Открываем страницу (можно заменить на selects2.html)
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим элементы с числами и получаем их текст
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # 2. Вычисляем сумму
    sum_result = int(num1) + int(num2)
    print(f"Найдена сумма: {num1} + {num2} = {sum_result}")

    # 3. Работа с выпадающим списком
    # Находим элемент <select> по его ID
    select_element = browser.find_element(By.ID, "dropdown")
    # Создаем объект Select для работы с выпадающим списком
    select = Select(select_element)

    # Выбираем опцию по видимому тексту (равному сумме)
    select.select_by_visible_text(str(sum_result))
    # Альтернативные способы:
    # select.select_by_value(str(sum_result))  # по атрибуту value
    # select.select_by_index(sum_result)       # по индексу (не рекомендуется, т.к. числа могут быть вразнобой)

    # 4. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # 5. Ждем результат и получаем код из алерта
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Код из алерта: {alert_text}")
    alert.accept()

finally:
    # Закрываем браузер
    time.sleep(2)
    browser.quit()