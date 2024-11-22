# ����������� ����������� ����������
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# ��������� ������� � ��������� ��������
driver = webdriver.Chrome()
driver.get("https://only.digital")
time.sleep(4)

# ����� ���������
try:
    element_Footer = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer")
    print("Footer = "������� ������")
except NoSuchElementException:
    print("������� �� ������")

try:
    element_span_VK = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[2]/a/span")
    print("VK span = "������� ������")
except NoSuchElementException:
    print("VK span = "������� �� ������")

try:
    element_span_Telegram = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[1]/div[2]/div[2]/div/div[3]/a/span")
    print("Telegram span = "������� ������")
except NoSuchElementException:
    print("Telegram span = "������� �� ������")

try:
    element_buttonUP = driver.find_element_by_xpath("/html/body/div[1]/div[5]/main/div[1]/footer/div[2]")
    print("Button UP = "������� ������")
except NoSuchElementException:
    print("Button UP = "������� �� ������")


driver.quit()
