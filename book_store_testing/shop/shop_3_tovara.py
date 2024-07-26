import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()

window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
time.sleep(4)
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
btn_html = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/aside/div[3]/ul/li[2]/a").click()
html_num = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/aside/div[3]/ul/li[2]")
assert "3" in html_num.text

time.sleep(4)
driver.quit()

