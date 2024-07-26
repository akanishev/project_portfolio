from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")

# Пройти авторизацию.
btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()

# Перейти в магазин и добавить  книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm" в корзину.
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
book_html5 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
book_js_data = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[5]/a[2]").click()
driver.execute_script("window.scrollBy(0, 300);")#Проскролить на 300 пикселей.
time.sleep(3)

# Перейти в корзину.
btn_basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]").click()
time.sleep(4)

# Удалить товар 1 позиции.
delete_book_html5 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[1]/a").click()
time.sleep(10)

# Отменить удаление товара.
btn_undo = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/a").click()

# Изменить количество товара.
quantity_book_js = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
quantity_book_js.clear()
time.sleep(2)
quantity_book_js.send_keys("3")
btn_update_basket = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[3]/td/input[1]").click()
time.sleep(4)

# Сверить что количество товара 1 позиции = 3.
quantity_book = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
assert quantity_book.get_attribute("value") == "3"
print("Колличество книг:3.")

# Применить купон.
btn_apply_coupon = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[3]/td/div/input[2]").click()
time.sleep(3)

# Cверить что текст уведомления соответствует требованию.
text_window = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/ul")
time.sleep(3)
quantity_book_js = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[2]/td[5]/div/input")
assert "Please enter a coupon code." == text_window.text
print("Тест пройден успешно")
driver.quit()
