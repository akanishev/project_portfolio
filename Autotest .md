# »мпортируем необходимые библиотеки
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# ќткрываем браузер и указанную страницу
driver = webdriver.Chrome()
driver.get("https://only.digital")
time.sleep(4)

# ѕоиск элементов
try:
    element_Footer = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer")
    print("Footer = "Ёлемент найден")
except NoSuchElementException:
    print("Ёлемент не найден")

try:
    element_span_VK = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[2]/a/span")
    print("VK span = "Ёлемент найден")
except NoSuchElementException:
    print("VK span = "Ёлемент не найден")

try:
    element_span_Telegram = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[3]/a/span")
    print("Telegram span = "Ёлемент найден")
except NoSuchElementException:
    print("Telegram span = "Ёлемент не найден")

try:
    element_buttonUP = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[2]")
    print("Button UP = "Ёлемент найден")
except NoSuchElementException:
    print("Button UP = "Ёлемент не найден")


driver.quit()
