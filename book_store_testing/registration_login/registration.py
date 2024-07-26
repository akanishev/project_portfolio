import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
#Регистрация аккаунта.
window_email = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[1]/input").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[2]/input").send_keys("testpassword251694/")
btn_register = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]").click()
time.sleep(4)

driver.quit()