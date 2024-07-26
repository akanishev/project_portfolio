import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")

# Авторизация
btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()

#Добавить книгу HTML5 WebApp Develpment в корзину.
btn_add_to_basket = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
count_basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]")
price_basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[2]")
time.sleep(5)
# Добавить явное ожидание.
price_check = WebDriverWait(driver,20).until(
     EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[2]"), "180.00")
)
count_check = WebDriverWait(driver,20).until(
     EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]"), "1")
)
btn_basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/i").click()
count_total = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[6]/span")
count_subtotal = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div/table/tbody/tr[1]/td/span")
assert "180.00" in count_total.text
assert "180.00" in count_subtotal.text
print("Тест успешно пройден!")
driver.quit()
