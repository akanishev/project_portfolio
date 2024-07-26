import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

#Авторизоваться
btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
time.sleep(4)
#Перейти в магазин и открыть книгу Android Quick Start Guide. 
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
btn_book_android_quick_start = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[1]/a[1]/h3").click()
#Убедиться что содержимое старой цены = 600.00, а новой = 450.00
old_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/del/span")
new_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/ins/span")

assert  "600.00" in old_price.text
assert  "450.00" in new_price.text

btn_cardbook = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[1]/a/img").click()
btn_close = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a")))
btn_close.click()

driver.quit()
