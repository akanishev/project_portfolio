import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")

btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()

window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
time.sleep(4)
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
select_default_sorting = driver.find_element_by_css_selector("[value='menu_order'")
assert "Default sorting" in select_default_sorting.text
time.sleep(3)
selector = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/select")
select = select(selector)
select.select_by_value("price-desc")

assert "Sort by price: high to low" in selector.text
print("Тест успешно завершен")

driver.quit()

