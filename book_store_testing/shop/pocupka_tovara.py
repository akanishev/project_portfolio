import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://practice.automationtesting.in/")
# Пройти авторизацию.
btn_my_account_menu = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
window_email = driver.find_element_by_css_selector("#username").send_keys("a.test@gmail.com")
window_password = driver.find_element_by_css_selector("#password").send_keys("testpassword251694/")
btn_login = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]").click()
print("Авторизация прошла успешно")
btn_shop = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
driver.execute_script("window.scrollBy(0, 300);")
btn_add_book_html5 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
btn_basket = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]").click()
btn_proceed_to_checkout = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div > div > div > a")
btn_proceed_to_checkout.click()
#Создаем переменные обязательных полей для доставки заказа.
WebDriverWait(driver,20).until(   #Явное ожидание для поля first name.
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[1]/div[1]/div/p[1]/input"))
)
first_name = driver.find_element_by_css_selector("#billing_first_name")
last_name = driver.find_element_by_css_selector("#billing_last_name")
email = driver.find_element_by_css_selector("#billing_email")
number_phone = driver.find_element_by_css_selector("#billing_phone")
#Вввести в селекторе Russia и выбрать из списка.
country_selector = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[1]/div[1]/div/p[6]/div")
country_selector.click()
country_imput = driver.find_element_by_css_selector("#s2id_autogen1_search")
country_imput.send_keys("Russia")
country_option = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#select2-results-1 > li"))
)
country_option.click()
address = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[1]/div[1]/div/p[7]/input")
city = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[1]/div[1]/div/p[9]/input")
postcode = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[1]/div[1]/div/p[11]/input")
#Перед вводом данных очистить поля.
first_name.clear()
last_name.clear()
email.clear()
number_phone.clear()
address.clear()
city.clear()
postcode.clear()
print("Старые данные успешно удалены.")
#Ввести данные в обязательные поля.
first_name.send_keys("Alexander")
last_name.send_keys("Petrov")
email.send_keys("a.test@gmail.com")
number_phone.send_keys("+79234567558")
address.send_keys("Zabalueva 45")
city.send_keys("Moscow")
postcode.send_keys("390000")
print("Новые данные успешно введенны.")
checkbox_check_payment = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[2]/div/ul/li[2]/input").click()
btn_place_order = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form[2]/div[2]/div/div/input[1]")
btn_place_order.click()
print("Тест успешно завершен!")
driver.quit()