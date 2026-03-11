from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome() # измени Edge() на нужный драйвер
    browser.get(link)

    # После перехода по ссылке ищем поля формы и заполняем их
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input1_1 = browser.find_element(By.CSS_SELECTOR,"div.form-group.second_class input.form-control.second")
    input1_1.send_keys("Petrov")
    input2 = browser.find_element(By.CLASS_NAME, "third")
    input2.send_keys("Petrov@mail.ru")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]')
    input3.send_keys("111 111 111")
    input4 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст тег <h1>
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()