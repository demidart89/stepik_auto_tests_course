from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@example.com")

    # 2. Создаем файл для загрузки
    # Получаем путь к текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'bio.txt')

    # Создаем текстовый файл (если его нет)
    with open(file_path, 'w') as file:
        file.write("This is my short bio.")

    # 3. Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # 4. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # 5. Получаем результат
    time.sleep(5)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(f"Код из алерта: {alert_text}")
    alert.accept()

finally:
    # Закрываем браузер
    time.sleep(2)
    browser.quit()