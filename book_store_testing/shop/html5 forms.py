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
btn_book_html_5_forms = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[1]/h3").click()
header_name_book_html_5_forms = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/h1")
header_name_book_html_5_forms_text = header_name_book_html_5_forms.text
assert "HTML5 Forms" in header_name_book_html_5_forms_text

driver.quit()