import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

# Перейти в раздел отзыва.
btn_selenium_ruby = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/ul/li/a[1]/h3")
driver.execute_script("window.scrollBy(0, 600);") # Проскролить страницу на 600 пикселей.
time.sleep(3)
btn_selenium_ruby.click()
driver.execute_script("window.scrollBy(0, 500);") # Проскролить страницу на 500 пикселей.
time.sleep(2)
btn_reviews = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/ul/li[2]/a").click()

# Поставить оценку 5 звезд, заполнить поля данными и отправить комментарий.
btn_ocenka = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/form/p[2]/p/span/a[5]").click()
window_you_review = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/form/p[3]/textarea").send_keys("Nice book!")
window_name = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/form/p[4]/input").send_keys("Alexander")
window_email = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/form/p[5]/input").send_keys("a.test@gmail.com")
btn_submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div/form/p[7]/input[1]").click()
time.sleep(2)
driver.quit()
